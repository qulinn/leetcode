def largestAltitude(gain: list) -> int:
    current_altitude = 0
    highest_point = current_altitude

    for i in gain:
        current_altitude += i
        highest_point = max(highest_point, current_altitude)
    
    return highest_point

def main():
    # Input: 
    gain = [-4,-3,-2,-1,4,3,2]
    # Output: 
    expected_output = 0
    assert largestAltitude(gain) == expected_output

if __name__ == '__main__':
    main()