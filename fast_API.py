from fastapi import FastAPI

app = FastAPI()


food_items  = {"Indian":["roti", "Dal"],
               "Italian": ["pizza", "pasta"],
               "Mexican" : ["tacos","burrito"],
               "american": ["burger", "french fries"]}


@app.get("/foods/{cuisine}")
async def get_items(cuisine):
    food = food_items.get(cuisine)
    if food:
        return food
    else:
        msg = f"We are really sorry, but we do not have any kind of {cuisine} food you asked for."
        return msg

@app.get("/hello/{name}")
async def hello(name):
    k = f"welcome {name}"
    return k

@app.get("/")
async def main():
    return "welcome to home page. This is Continental Restaurant."