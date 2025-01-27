# SafeGraph Semester Project

1. Please read the [Statement of Need](needs_statement.md) that your team will need to leverage to write your work proposal.
2. Use the [team_repo template](https://github.com/BYUI451/team_repo) for your writeup and submission.
    - Please make sure your team repo is private.
    - You will need to share your repo with me, `hathawayj`, and the current semester team.
3. Use this template repo to start your private repo within our organization. This repo will allow you to practice and share your personal work.
4. Review the scripts in this repo and ensure you can handle the SafeGraph data. Within two weeks, we will have a coding challenge using SafeGraph data.

## Scripts

The scripts in this template repository can help you get a picture of digesting the SafeGraph format.

### [`eda_safegraph.r`](eda_safegraph.r)

This script depends on the Tidyverse and has two parsing functions at the top. There are some examples throughout the script of the issues with handling the SafeGraph data. The final `dat_all` object provides the full call that processes the data into a clean nested Tibble.
### [`eda_safegraph.py`](eda_safegraph.py)

This script depends on the `safegraph_functions.py` file for some functions that can parse the nested dictionaries and lists within the POI. The Python functions create new data objects of the list and dictionary variables within the dataset.

### API Examples

SafeGraph has an API to request data. We will use the API to build our datasets for use in Spark. We can figure out the API locally first.
#### [`graphql_noath.py`](graphql_noauth.py)

An elementary API example of letting you evaluate that your system can make calls to a GraphQL API. It only uses the `requests` package in Python.
#### [`graphql_safegraph.py`](graphql_safegraph.py)

This script is the more extended and diverse example of using a GraphQL API. Specifically, it provides three examples of requesting data from the SafeGraph API.

Note the use of the following lines of code to store and retrieve our API key correctly. This code is also exemplified in [`create_environ.py`](create_environ.py) script.

```python
import os
from dotenv import load_dotenv

load_dotenv()
sfkey = os.environ.get("SAFEGRAPH_KEY")
```

We use three Python packages to get data from SafeGraph - `gql`, `requests`, and `safegraphql`. We elected to signal the start of each type of API request with the package imports spread throughout the script.

We will focus on the `gql` or `requests` examples for our work. I want to stay in `gql`.

#### [`parse_safegraph.py`](parse_safegraph.py)

This file creates `.parquet` files for upload for our cloud compute.  In addition, it breaks all the nested data out into their own tables.

## SafeGraph Guides

You can see a [Colab notebook](https://colab.research.google.com/drive/1cs9qq_MWppKF4DQ0Xl3lyesHEnsc4D6D#scrollTo=_s0TsIZclcbe) that guides you through parsing data from shop.safegraph.com.

SafeGraph has a a light technical quickstart guide to working with POI and Mobility data downloaded from the [SafeGraph Shop](https://shop.safegraph.com/), the self-serve source for hundreds of datasets about physical places. The goal of their guide is to get you working effectively with the SafeGraph data as fast as possible.

They filmed a series of YouTube videos which provide context for each step:

- [SafeGraph Shop Python Quickstart Part 1: Data Preparation](https://www.youtube.com/watch?v=e0X1EwBew_M)
- [SafeGraph Shop Python Quickstart Part 2: Exploding Nested JSON Fields](https://www.youtube.com/watch?v=j3A_xX7Hwqo)
- [SafeGraph Shop Python Quickstart Part 3: Joining to Census Data](https://www.youtube.com/watch?v=OQf9jCI_ltc)
- [SafeGraph Shop Python Quickstart Part 4: Scaling](https://www.youtube.com/watch?v=BvDsHJNEkU0)

They recommend joining the [SafeGraph Community Slack Channel](https://readme.safegraph.com/docs/join-our-community), a fantastic resource for live, in-person support. Finally, check out their [documentation](https://docs.safegraph.com/docs) for an exhaustive guide to our data.

### Open Census Neighborhood Demographics Data

- [Download Open Census Data & Neighborhood Demographics](https://www.safegraph.com/free-data/open-census-data)