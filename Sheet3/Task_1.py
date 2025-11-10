import numpy as np
import matplotlib.pyplot as plt


def is_in_ellipsoid(a, b, c, r, point):
    x, y, z = point
    return (x**2) * a + (y**2) * b + (z**2) * c < r


def acception_rejection(a, b, c, r, number_of_sample_points):
    accepted_points = []
    rejected_points_count = 0
    while len(accepted_points) < number_of_sample_points:
        x_new = np.random.uniform(- np.sqrt(r/a), np.sqrt(r/a))
        y_new = np.random.uniform(- np.sqrt(r/b), np.sqrt(r/b))
        z_new = np.random.uniform(- np.sqrt(r/c), np.sqrt(r/c))
        new_point = (x_new, y_new, z_new)
        if is_in_ellipsoid(a, b, c, r, new_point):
            accepted_points.append(new_point)
        else:
            rejected_points_count += 1
    print(f"Number of accepted points: {len(accepted_points)}")
    print(f"Number of rejected points: {rejected_points_count}")
    probability = number_of_sample_points / (number_of_sample_points + rejected_points_count)
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
