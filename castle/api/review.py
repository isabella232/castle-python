from castle.api_request import APIRequest
from castle.commands.review import CommandsReview


class APIReview(object):
    @staticmethod
    def retrieve(review_id):
        return APIRequest().call(CommandsReview.build(review_id))
