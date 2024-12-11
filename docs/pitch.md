# VERY VERY rough outline, will make prettier later

Authors: Amelia, Chiara and Gbemi 
# Research questions:  

1. How does economic periods (measured through GDP) affect art themes in America? 
  a. Historically, the countries that have tended to be richer have also made more artworks (such as the roman empire and Greek empire making lots of statues and artworks throughout their more successful periods). Therefore, we wondered whether there was any correlation between the art themes present in a certain country and the economic well being of that country. We chose America because it is the hub of economic activity and therefore if might be interesting to see if it has a strong correlation between popular art themes. 
2. How do social movements affect recent art themes in America? 

We chose this to get a broader perspective on what affects art themes in America and build on our findings from question 1. 
 
# Data sources: 
* FRED – gather real GDP from 1929 to 2023. We will create a function to get the annual percentage change in real GDP per year to analyse whether the economy is in boom or recession. Chose this because it has data on America dating back to 1929 which allows us to look at a larger time period than other APIs. 
Does not need a key 
Rate limit: 120 requests per minute 
Json format 
Endpoints: Includes endpoints for series data, categories, sources, and economic releases. 
Numerical time-series data related to economic metrics like GDP, unemployment, interest rates, inflation, etc. 
Highly structured and easy to parse 
Processing needs: Normalization- Time-series data may need transformation for analytics (e.g., seasonally adjusted data). If there is a range of years, we will change the data to only contain the start year for ease of analysis. (This will also be done with the other two APIs) 
 
* Reddit – scrape data searching social movement tags e.g ‘black lives matter’. Look at the frequency of tags of a social movement and check whether this trends with the emergence of new art themes or the frequency of art themes being created. Chose this as it has social movement tags organised into subreddits so we can find information on social movements easily. Reddit is also older than Twitter so we can look at a more comprehensive data set. 
Needs an access key- create an application in Reddit's developer portal. This process provides you with a client ID and a client secret, which are used to authenticate requests. 
Request limit: 60 per minute per user but can be expanded depending on usage and agreement with Reddit. We may need to design our system to stay within these limits or implement rate limiting to avoid getting temporarily blocked. 
Json format 
Endpoints: hot, new, top, and search endpoints for post data. Comment and user profile endpoints. 
User-generated content, including posts, comments, upvotes, and metadata. 
Highly unstructured text data. Data can be noisy. 
Data processing: Natural Language Processing (NLP)- For analysing themes, sentiment, and keyword extraction. It might have to be used depending on the volume of data we extract; Filtering: Removing irrelevant posts, spam, or non-English content. 
   
* Smithsonian Institution API- We will scrape data of all American art from 1929 to 2023 to look at the themes of this art. We will use this for both the first and second question. Chose this because it has a lot of data on American art ( with 11 million artworks) and it clearly categorises its art into topics (aka themes) therefore allowing us to analyse this data. 
Requires an access key: obtain by registering through the api.data.gov portal​ , GitHub , Postman API Platform . 
There is no strict request limit for the Smithsonian API, but it encourages developers to use the service responsibly and avoid excessive requests that might disrupt its systems.  
Json format 
Metadata about artifacts and artworks in the Smithsonian collection. 
Well organised and easy to query. Medium ease of use – rich but nuanced data. 
Endpoints: Object search (e.g., by keyword, themes, or artist).; Fetching metadata for specific objects.; Retrieving media (e.g., images, videos). 
Data processing: Extract and standardize themes, artists, and periods. 
 
# Timeline: 
 
Risks: 
1. Technical Issues 
API Rate Limits: 
Exceeding request limits for FRED (120/min), Reddit (60/min), or Smithsonian API (unspecified but potential throttling). 
Downtime or Changes in API: 
Unexpected downtime, deprecation of endpoints, or changes to API functionality. 
Data Overload: 
Large datasets from Smithsonian or Reddit can slow processing and overwhelm storage or computational resources. 
2. Data Quality Issues 
Incomplete Data: 
FRED may lack microeconomic context or metadata for deeper interpretations. 
Smithsonian entries might miss detailed thematic tags for all artworks. 
Noisy Data: 
Reddit content can include spam, irrelevant posts, or off-topic discussions. 
Bias or Gaps: 
Data might reflect institutional or user biases (e.g., underrepresentation of certain themes in Smithsonian collections or Reddit). 
3. Analytical Risks 
Theme Attribution: 
Assigning art themes to economic or social periods is inherently interpretive and may lead to subjective conclusions. 
Correlations vs. Causations: 
Economic periods and social movements’ impacts on art are complex and multifactorial, risking oversimplified conclusions. 
4. Ethical and Legal Risks 
Data Privacy: 
Scraping Reddit user data must comply with ethical guidelines and Reddit’s terms of service. 
Copyright Concerns: 
Using Smithsonian media may require adherence to usage rights. 
 
# Backup plan: 
1. For Technical Issues 
Redundancy in APIs: 
Use alternate APIs if one fails: 
For economic data: World Bank API or OECD API. 
For art metadata: Europeana API or other open-access museum APIs. 
For social sentiment: Twitter API as an alternative to Reddit. 
Rate-Limiting Solutions: 
Implement request queuing and caching to stay within rate limits. 
Utilize API-provided bulk download options, like Smithsonian's collections dump. 
Use time.sleep() to limit the requests 
Local Backup: 
Download and store datasets locally for continued analysis if APIs become inaccessible. 
2. For Data Quality Issues 
Preprocessing Pipelines: 
Develop robust data cleaning processes: 
NLP models for Reddit (e.g., spam detection and topic modeling). 
Validation scripts for metadata completeness in Smithsonian datasets. 
Other Sources: 
Use academic and institutional reports or curated datasets for missing thematic data or validation. 
3. For Analytical Risks 
Iterative Analysis: 
Use peer reviews to validate findings. 
Transparent Reporting: 
Clearly state assumptions, limitations, and potential biases in the project's findings. 
4. For Ethical and Legal Risks 
Compliance with Terms: 
Review and strictly adhere to API terms of service and usage policies. 
Data Privacy Safeguards: 
Anonymize Reddit user data and focus on aggregated insights. 
 
# Contributions: 
 
 
Contribution (%) 
Data collection (%) 
Data Cleaning (%) 
Visualisations (%) 
Repository Organisations (%) 
Documentation (%) 
Amelia 
30 
30 
50 
10 
40 
Chiara 
30 
30 
50 
20 
30 
Gbemi 
30 
30 
N/A 
70 
30 
 
Amelia – Reddit 
Gbemi - FRED 
Chiara - Smithsonian 
