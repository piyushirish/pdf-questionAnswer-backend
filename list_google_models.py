from google.ai.generativelanguage import ModelServiceClient

def list_models():
    client = ModelServiceClient()
    print("Available models:")
    models = client.list_models()
    for model in models:
        print(model.name)

if __name__ == "__main__":
    list_models()
