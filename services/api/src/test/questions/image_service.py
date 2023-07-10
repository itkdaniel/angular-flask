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


# Given the root of a binary tree, return the leftmost value in the last row of the tree.
"""
			2
		1		3
- return 1	
"""

class TreeNode(object):
	def __init__(self,val=0,left=None,right=0):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lmap = self.group_by_level(root, 0, defaultdict(list))
        return	lmap[max(lmap.keys())][0].val

    def group_nodes_by_level(self, root, level, levels_map):
    	# level starts at 0
		levels_map[level].append(root)
		if root.left:
			self.group_by_level(root.left, level+1, levels_map)
		if root.right:
			self.group_by_level(root.right, level+1, levels_map)
		return levels_map

	def bstdeepleft(lmap):
		return lmap[max(lmap.keys())][0]

	# def get_smallest_from_deepest(self, levels_map):
	# 	left_most = lambda d: map(lambda: ) 
from collections import defaultdict

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)
one.left = two
one.right = three
two.left = four
three.left = five
three.right = six
five.left = seven

bottomleft = Solution().findBottomLeftValue(one)

lmap = Solution().group_by_level(one, 0, defaultdict(list))

mapping = {key:[item.val for item in value] for key,value in lmap.items()}
bottomleft = Solution().deepleft(mapping)

## OR

levels = zip(lmap.keys(), lmap.values())
groups = {level[0]:[g.val for g in level[1]] for level in levels}
bottomleft = groups[max(groups.keys())][0]



# [3,2,null,1,-2147483648]
"""
				3
			2	null
		1	-2147



"""