import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foodCuisine = {}
        self.foodRating = {}
        self.cuisineHeap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodCuisine[food] = cuisine
            self.foodRating[food] = rating
            if cuisine not in self.cuisineHeap:
                self.cuisineHeap[cuisine] = []
            heapq.heappush(self.cuisineHeap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        cuisine = self.foodCuisine[food]
        self.foodRating[food] = newRating
        heapq.heappush(self.cuisineHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisineHeap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.foodRating[food]:
                return food
            heapq.heappop(heap)
