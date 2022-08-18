# CCC Group Project Team 30
## Description
Covid-19 (Coronavirus) pandemic has been the top challenge of public health over the world since February 2020. With the first and the most number of historical confirmed cases in Australia, Victoria has suffered from several outbreaks until yet. There have been three city lockdowns in Victoria due to the outbreaks from March 2020 to March 2021. Along with the outbreaks and city lockdowns, a public panic phenomenon arose as a potential crisis in the society. 
As the main tool of networking and expression during periods of social distance restrictions, social media captured enormous information and opinions about the pandemic. With well documented and open-sourced APIs,  Twitter provides rich and high quality data of its users and posts named “tweet”, allowing researchers to gain insight from social media analysis. This  paper introduces a cloud-based platform exploring the Victorian public sentiment through different stages of the Covid-19 pandemic. The pandemic started from March 2020 in Victoria as shown in Figure 6.1. Therefore the timeline of our analysis starts from March 2020. Specifically, using natural language processing, the sentiment levels of different statistical regions in Victoria are analyzed and visualized. The pandemic sentiment levels in Melbourne which is the main city of Victoria are further compared to the non-pandemic sentiment levels in 2015 and 2017. Several kinds of regional data are encompassed to evaluate the potential correlations between public sentiment and factors such as national economy, employment situation and age distribution during the pandemic period in 2020. In addition, the harvester application provides a real-time analysis of sentiment and visualization of up-to-date hot topics on Twitter, tracking the public sentiment in Victoria along the continuing Covid-19 pandemic.


## Team Member
* [Xinyu Zeng- 1234798](https://github.com/jadeyyuu)
* [Yuxuan Liu - 743365](https://github.com/PatrickLiuyx)
* [Jing Yang - 1250442](https://github.com/ChelseaYang1130)
* [Yilin Yu - 965720](https://github.com/Hieler)
* [Chen Zhou - 987776](https://github.com/CZZHO)

## Demonstration Video links
 - Ansible: https://youtu.be/2rKPK4ZUcn4
 - CouchDB: https://youtu.be/9TnfqdsxSR8 
 - Web Platform: https://youtu.be/gCVeuToZgzY


## Project Structure

### Deployment Operation 
1. Ansible creates 4 hosts with one click
2. Docker runs 3 CouchDB instances
3. Ansible controls Docker-compose with services on each instances 

### Websever
1. Front-end deployed by Bootstrap v5.0 and jQuery
2. Back-end deployed by Django
3. CouchDB related interface
3. Object Storage interface
4. Data query interface
5. Interface joint debugging

### Historical Data Analysis
1. Pyspark DataFrame API
   - Pyspark SQL for statistical analysis
   - Pyspark MLib for Latent Dirichlet Allocation topic modelling
   - Textblob for NLP sentiment analysis
2. tweepy for steaming tweet collection
3. Plotly for interative data visulization
4. Interate with CouchDB:
   - Retrieve historical tweets data
   - Save and retrieve streaming tweets data
   - Save visualization indexes in json format

### Couchdb
Store and retrieve data from the couchdb


### Server Arrangement
Server1: 172.26.130.42
<br />Docker/
<br />CouchDB/ 
<br />Frontend/
<br />    
Server2: 172.26.131.236
<br />CouchDB/
    <br />Spark/
    <br />Backend/
    <br />Twitter API/
 <br />   
Server3: 172.26.134.19
   <br /> CouchDB/ couchdb:2.3.0
    <br />Backend/
    <br />Straming API/
 <br />  
Server4: 172.26.129.75
    <br />Aurin/
    <br />Investing/
Notes: This web platform has deployed by intranet, you have to contact [Unimelb](https://studentit.unimelb.edu.au/) to get VPN acess. 
    
    
    








