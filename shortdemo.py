from allennlp.models.archival import load_archive
from allennlp.predictors import Predictor

archive = load_archive(
            "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz"
        )
predictor = Predictor.from_archive(archive, 'constituency-parser')

print("we are here")
predictor.predict_json({"sentence": "This is a sentence to be predicted!"})

predictor.predict_instance()