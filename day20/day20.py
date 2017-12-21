# Particle Swarm

import sys


# Find the particle which will stay closest to <0, 0, 0>
# In other words, take limit(time->infinity) Manhattan(<a>)
def part1(particles):
    # Find particle(s) with smallest acceleration
    min_accel = sys.maxint
    for i in range(0, len(particles)):
        # Calculate Manhattan Distance
        mh_accel = abs(particles[i][2][0]) + abs(particles[i][2][1]) + abs(particles[i][2][2])
        if mh_accel < min_accel:
            min_accel = mh_accel
    contenders = []
    for i in range(0, len(particles)):
        mh_accel = abs(particles[i][2][0]) + abs(particles[i][2][1]) + abs(particles[i][2][2])
        if mh_accel == min_accel:
            contenders.append(i)
    # We may have multiple particles with the same acceleration,
    # so now we must take the limit on their velocities
    min_vel = sys.maxint
    for i in contenders:
        mh_vel = abs(particles[i][1][0]) + abs(particles[i][1][1]) + abs(particles[i][1][2])
        if mh_vel < min_vel:
            min_vel = mh_vel
    last_contenders = []
    for i in contenders:
        mh_vel = abs(particles[i][1][0]) + abs(particles[i][1][1]) + abs(particles[i][1][2])
        if mh_vel == min_vel:
            last_contenders.append(i)
    del contenders
    # We may have multiple particles with the same velocity,
    # so now we must take the limit on their position
    min_pos = sys.maxint
    index = 0
    for i in last_contenders:
        mh_pos = abs(particles[i][0][0]) + abs(particles[i][0][1]) + abs(particles[i][0][2])
        if mh_pos < min_pos:
            min_pos = mh_pos
            index = i
    del last_contenders
    return index


# Find index of nth occurence of char in string
def find_nth(string, char, n):
    count = 0
    for i in range(0, len(string)):
        if string[i] == char:
            count += 1
        if count == n:
            return i
    return None


# Build list of [ [pos], [vel], [accel] ]
def build_particle_map(lines):
    particles = []
    for line in lines:
        pos_str = line[find_nth(line, "<", 1) + 1: find_nth(line, ">", 1)]
        pos = [ int(x) for x in pos_str.split(',') ]
        vel_str = line[find_nth(line, "<", 2) + 1: find_nth(line, ">", 2)]
        vel = [ int(x) for x in vel_str.split(',') ]
        accel_str = line[find_nth(line, "<", 3) + 1: find_nth(line, ">", 3)]
        accel = [ int(x) for x in accel_str.split(',') ]
        particles.append( [ pos, vel, accel ] )
    return particles


# Evaluate position at each time step, remove all colliding particles, continue
def run_simulation(particles, num_iters):
    for i in range(0, num_iters):
        hash_pos = {}
        # Build hash_map of positions at current time
        for i in range(0, len(particles)):
            # Update velocities
            particles[i][1][0] += particles[i][2][0]
            particles[i][1][1] += particles[i][2][1]
            particles[i][1][2] += particles[i][2][2]
            # Update positions
            particles[i][0][0] += particles[i][1][0]
            particles[i][0][1] += particles[i][1][1]
            particles[i][0][2] += particles[i][1][2]
            # Hash it
            try:
                count, indices = hash_pos[ tuple(particles[i][0]) ]
                count += 1
                indices.append(i)
            except KeyError:
                hash_pos[ tuple(particles[i][0]) ] = 0, [i]
        # Iterate over dict
        for key in hash_pos.keys():
            count, indices = hash_pos[key]
            if count > 1:
                print key, hash_pos[key]


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    # Build particle map
    particles = build_particle_map(lines)
    # Find particle that stays closest to 0
    print part1(particles)
    # Take the limit as time goes to infinity
    # run_simulation(particles, int(sys.argv[2]))
