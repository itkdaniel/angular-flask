import heapq
import time
from collections import defaultdict

class ImageService:

	def __init__(self):
		self.images = []
		self.image_map = defaultdict(set) # {image_id: image(timestamp, imageid, metadata)}

	def store_image(self, image_id, timestamp, metadata):
		image = (timestamp, image_id, metadata)
		heapq.heappush(self.images, image)
		self.image_map[image_id] = image

	def get_most_recent_images(self, n):
		recent_images = heapq.nlargest(n, self.images)
		return [image[1] for image in recent_images]

	def get_image_in_range(self, start, end):
		images_in_range = []
		for image in self.images:
			timestamp = image[0]
			if start <= timestamp <= end:
				images_in_range.append(image[1])
			elif timestamp < start:
				break
		return images_in_range

	def remove_image(self, image_id):
		if image_id in self.image_map:
			image = self.image_map(image_id)
			self.images.remove(image)
			heapq.heapify(self.images)
			del self.image_map[image_id]