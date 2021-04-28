{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6e4286f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyspark.sql import SparkSession\n",
    "from pyspark.sql.functions import *\n",
    "from pyspark.sql.types import *\n",
    "from pyspark.sql import functions as F\n",
    "from textblob import TextBlob\n",
    "from pyspark.sql import SQLContext"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d1effc3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyspark.sql.types import StringType\n",
    "\n",
    "from nltk.stem.wordnet import WordNetLemmatizer\n",
    "from nltk.corpus import stopwords\n",
    "from nltk import pos_tag\n",
    "import string\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a2f55ffe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# remove non ASCII characters\n",
    "def strip_non_ascii(data_str):\n",
    "    ''' Returns the string without non ASCII characters'''\n",
    "    stripped = (c for c in data_str if 0 < ord(c) < 127)\n",
    "    return ''.join(stripped)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "aa853887",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fixed abbreviation\n",
    "def fix_abbreviation(data_str):\n",
    "    data_str = data_str.lower()\n",
    "    data_str = re.sub(r'\\bthats\\b', 'that is', data_str)\n",
    "    data_str = re.sub(r'\\bive\\b', 'i have', data_str)\n",
    "    data_str = re.sub(r'\\bim\\b', 'i am', data_str)\n",
    "    data_str = re.sub(r'\\bya\\b', 'yeah', data_str)\n",
    "    data_str = re.sub(r'\\bcant\\b', 'can not', data_str)\n",
    "    data_str = re.sub(r'\\bdont\\b', 'do not', data_str)\n",
    "    data_str = re.sub(r'\\bwont\\b', 'will not', data_str)\n",
    "    data_str = re.sub(r'\\bid\\b', 'i would', data_str)\n",
    "    data_str = re.sub(r'wtf', 'what the fuck', data_str)\n",
    "    data_str = re.sub(r'\\bwth\\b', 'what the hell', data_str)\n",
    "    data_str = re.sub(r'\\br\\b', 'are', data_str)\n",
    "    data_str = re.sub(r'\\bu\\b', 'you', data_str)\n",
    "    data_str = re.sub(r'\\bk\\b', 'OK', data_str)\n",
    "    data_str = re.sub(r'\\bsux\\b', 'sucks', data_str)\n",
    "    data_str = re.sub(r'\\bno+\\b', 'no', data_str)\n",
    "    data_str = re.sub(r'\\bcoo+\\b', 'cool', data_str)\n",
    "    data_str = re.sub(r'rt\\b', '', data_str)\n",
    "    data_str = data_str.strip()\n",
    "    return data_str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6a2b7e35",
   "metadata": {},
   "outputs": [],
   "source": [
    "def remove_features(data_str):\n",
    "    # compile regex\n",
    "    url_re = re.compile('https?://(www.)?\\w+\\.\\w+(/\\w+)*/?')\n",
    "    punc_re = re.compile('[%s]' % re.escape(string.punctuation))\n",
    "    num_re = re.compile('(\\\\d+)')\n",
    "    mention_re = re.compile('@(\\w+)')\n",
    "    alpha_num_re = re.compile(\"^[a-z0-9_.]+$\")\n",
    "    # convert to lowercase\n",
    "    data_str = data_str.lower()\n",
    "    # remove hyperlinks\n",
    "    data_str = url_re.sub(' ', data_str)\n",
    "    # remove @mentions\n",
    "    data_str = mention_re.sub(' ', data_str)\n",
    "    # remove puncuation\n",
    "    data_str = punc_re.sub(' ', data_str)\n",
    "    # remove numeric 'words'\n",
    "    data_str = num_re.sub(' ', data_str)\n",
    "    # remove non a-z 0-9 characters and words shorter than 1 characters\n",
    "    list_pos = 0\n",
    "    cleaned_str = ''\n",
    "    for word in data_str.split():\n",
    "        if list_pos == 0:\n",
    "            if alpha_num_re.match(word) and len(word) > 1:\n",
    "                cleaned_str = word\n",
    "            else:\n",
    "                cleaned_str = ' '\n",
    "        else:\n",
    "            if alpha_num_re.match(word) and len(word) > 1:\n",
    "                cleaned_str = cleaned_str + ' ' + word\n",
    "            else:\n",
    "                cleaned_str += ' '\n",
    "        list_pos += 1\n",
    "    # remove unwanted space, *.split() will automatically split on\n",
    "    # whitespace and discard duplicates, the \" \".join() joins the\n",
    "    # resulting list into one string.\n",
    "    return \" \".join(cleaned_str.split())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8f434d0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyspark.sql.types import FloatType\n",
    "\n",
    "from textblob import TextBlob\n",
    "\n",
    "def sentiment_analysis(text):\n",
    "\n",
    "    return TextBlob(text).sentiment.polarity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "69b0e88e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def condition(r):\n",
    "    if (r >=0.1):\n",
    "        label = \"positive\"\n",
    "    elif(r <= -0.1):\n",
    "        label = \"negative\"\n",
    "    else:\n",
    "        label = \"neutral\"\n",
    "    return label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2ec088a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "strip_non_ascii_udf = udf(strip_non_ascii, StringType())\n",
    "fix_abbreviation_udf = udf(fix_abbreviation, StringType())\n",
    "remove_features_udf = udf(remove_features, StringType())\n",
    "sentiment_analysis_udf = udf(sentiment_analysis , FloatType())\n",
    "sentiment_udf = udf(lambda x: condition(x), StringType())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14b12f0e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
