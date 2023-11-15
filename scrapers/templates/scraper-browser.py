from typing import TypedDict,List
from utils.browser import Browser

from utils.my_types import ProductListingInput,ProductListingOutput,ProductScraperInput,Variant

page=Browser()

# Product listing function
def product_listing(data:ProductListingInput)->ProductListingOutput:
	print(data)
	return {
		"site":data["site"],
		"urls":["https://test.com/"],
		"data":{}
	}

# Product scraping function
def product_scraping(data:ProductScraperInput)->List[Variant]:
	print(data)
	page.driver.get("https://www.ipify.org/")
	return []


