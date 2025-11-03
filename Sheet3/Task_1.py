import numpy as np
import matplotlib.pyplot as plt


def is_in_ellipsoid(a, b, c, r, point):
    x, y, z = point
    return (x**2) * a + (y**2) * b + (z**2) * c < r

def acception_rejection(a, b, c, r, number_of_sample_points):
    accepted_points = []
    x_sample_points = np.random.uniform(- np.sqrt(r/a), np.sqrt(r/a), number_of_sample_points)
    y_sample_points = np.random.uniform(- np.sqrt(r/b), np.sqrt(r/b), number_of_sample_points)
    z_sample_points = np.random.uniform(- np.sqrt(r/c), np.sqrt(r/c), number_of_sample_points)
    sample_points = np.array(list(zip(x_sample_points, y_sample_points, z_sample_points)))
    for point in sample_points:
        if is_in_ellipsoid(a, b, c, r, point):
            accepted_points.append(point)
    probability = len(accepted_points) / number_of_sample_points
    return accepted_points, probability



if __name__ == "__main__":
    a = 0.25
    b = 1
    c = 4
    r = 1

    cube_volume = (2 * np.sqrt(r/a)) * (2 * np.sqrt(r/b)) * (2 * np.sqrt(r/c))
    ellipsoid_volume = (4/3) * np.pi * (np.sqrt(r/a)) * (np.sqrt(r/b)) * (np.sqrt(r/c))

    N = 10000

    accepted_points, probability = acception_rejection(a, b, c, r, N)

    estimated_volume = probability * cube_volume
    print(f"Estimated Volume of the Ellipsoid: {estimated_volume}. Actual Volume: {ellipsoid_volume}")

    # Visualization
    accepted_points = np.array(accepted_points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(accepted_points[:, 0], accepted_points[:, 1], accepted_points[:, 2], s=1)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Points inside the Ellipsoid')
    plt.show()
