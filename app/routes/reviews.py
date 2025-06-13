from fastapi import APIRouter
from pydantic import BaseModel
from app.services import sentiment 

router = APIRouter()

class ReviewInput(BaseModel):
    product_name: str

@router.get('/sentiment/analyze')
def sentiment_analyze(review: ReviewInput):
    """
    This function is used to analyze the sentiment of the review
    """
    result = sentiment.sentiment_analyze(review.product_name)
    return result

# @router.post('/category/classify')
# def category_classify(review: ReviewInput):
#     """
#     This function is used to classify the category of the review
#     """
#     categories = sentiment.category_classify(review.product_name)
#     return {'categories': categories}

@router.post('/product/revieww-summary')
def product_review_summary(review: ReviewInput):
    """
    This function is used to get the summary of the review 
     """
    amazon_reviews = sentiment.scrape_amazon(review.product_name)
    noon_reviews = sentiment.scrape_noon(review.product_name)
    jumia_reviews = sentiment.scrape_jumia(review.product_name)

    amazon_result = sentiment.analyze_reviews(amazon_reviews)
    noon_result = sentiment.analyze_reviews(noon_reviews)
    jumia_result = sentiment.analyze_reviews(jumia_reviews)

    summary = sentiment.build_summary({
        "amazon": amazon_result,
        "noon": noon_result,
        "jumia": jumia_result
    })

    return summary
