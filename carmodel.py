import math

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = params['steering_angle']
    progress = params['progress']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    max_speed = 4.0  

    # Start with a low reward
    reward = 1e-3

    # Reward for staying on track
    if all_wheels_on_track:
        reward = 1.0

        # Reward higher speed
        reward += speed / max_speed

        # Reward smooth steering
        if abs(steering_angle) < 15:
            reward += 0.5

        # Reward progress along the track
        reward += progress / 100

        # Reward alignment with the track direction
        next_point = waypoints[closest_waypoints[1]]
        prev_point = waypoints[closest_waypoints[0]]
        track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
        track_direction = math.degrees(track_direction)
        direction_diff = abs(track_direction - heading)
        if direction_diff < 10:
            reward += 0.5

    # Penalize going off track
    else:
        reward *= 0.1

    # Return the reward as a float
    return float(reward)
