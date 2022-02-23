import redis

def main():
    redis = redis.StrictRedis(host='localhost', port=6379, db=0)
    model = DeepFace.build_model("Facenet")
    input_shape = (160, 160)

    # local unit test
    local_db = {
'angelina': 'deepface/tests/dataset/img2.jpg',
'jennifer': 'deepface/tests/dataset/img56.jpg',
'scarlett': 'deepface/tests/dataset/img49.jpg',
'katy': 'deepface/tests/dataset/img42.jpg',
'marissa': 'deepface/tests/dataset/img23.jpg'
}

if __name__ == '__main__':
    main()
