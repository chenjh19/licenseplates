from LocalBinaryPatternizer import LocalBinaryPatternizer

class Character:
    def __init__(self, value, corners, image):
        self.value   = value
        self.corners = corners
        self.image   = image

    # Testing purposes
    def show(self):
        from pylab import imshow, show
        imshow(self.data, cmap="gray")
        show()

    def get_feature_vector(self):
        pattern = LocalBinaryPatternizer(self.image)

        return pattern.create_features_vector()
