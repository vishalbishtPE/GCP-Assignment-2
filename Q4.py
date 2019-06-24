from google.cloud import vision
#The function localize_objects_uri(path), a Google Vision API to detect the objects
#in the image is called specifying the path of the image file.
#hello_gcs() function is triggered when an image is uploaded in the bucket.

def hello_gcs(data, context):
	"""Triggered by a change to a Cloud Storage bucket.
	Args:
	data (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
	"""
	try:
		bucket = data['bucket']		#Fetches bucket name of the image added 
		file = data['name']		#Fetches name of the image file loaded
    		    		
		path = "gs://"+bucket+"/"+file		#Create a path of the image file.		
		
		localize_objects_uri(path)		#Calling the function with the specifi	
	except Exception as e:
		print("ERROR")			
		raise e        
    
def localize_objects_uri(uri):
	"""Localize objects in the image on Google Cloud Storage
	Args:
	uri: The path to the file in Google Cloud Storage (gs://...)
	"""
	try:		
		client = vision.ImageAnnotatorClient()

		image = vision.types.Image()
		image.source.image_uri = uri

		objects = client.object_localization(
			image=image).localized_object_annotations

		print('Number of objects found: {}'.format(len(objects)))
		for object_ in objects:
			print('\n{} (confidence: {})'.format(object_.name, object_.score))
			print('Normalized bounding polygon vertices: ')
			for vertex in object_.bounding_poly.normalized_vertices:
				print(' - ({}, {})'.format(vertex.x, vertex.y))
	except Exception as e:
		print("ERROR")
		raise e		

