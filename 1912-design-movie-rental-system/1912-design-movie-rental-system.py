from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movieToShops = {}
        self.rentedList = []
        self.priceMap = {}

        for shop, movie, price in entries:
            if movie not in self.movieToShops:
                self.movieToShops[movie] = []
            self.movieToShops[movie].append((price, shop))
            self.priceMap[(movie, shop)] = price

        for movie in self.movieToShops:
            self.movieToShops[movie].sort()

    def search(self, movie: int) -> List[int]:
        if movie not in self.movieToShops or not self.movieToShops[movie]:
            return []
        return [shop for _, shop in self.movieToShops[movie][:5]]

    def findShopIndex(self, movie: int, shop: int, price: int) -> int:
        arr = self.movieToShops[movie]
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < (price, shop):
                left = mid + 1
            else:
                right = mid
        return right

    def findRentedIndex(self, movie: int, shop: int, price: int) -> int:
        arr = self.rentedList
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < (price, shop, movie):
                left = mid + 1
            else:
                right = mid
        return right

    def rent(self, shop: int, movie: int) -> None:
        price = self.priceMap[(movie, shop)]
        i = self.findShopIndex(movie, shop, price)
        del self.movieToShops[movie][i]
        j = self.findRentedIndex(movie, shop, price)
        self.rentedList.insert(j, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.priceMap[(movie, shop)]
        i = self.findRentedIndex(movie, shop, price)
        del self.rentedList[i]
        j = self.findShopIndex(movie, shop, price)
        self.movieToShops[movie].insert(j, (price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rentedList[:5]]
