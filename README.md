# CS50 AI Degrees

A breadth-first search algorithm is used to compute the shortest path between two actors in Hollywood, linking them via shared movie appearances.

## Contributions

`degrees.py`:

- `shortest_path`: Returns the shortest path from a source person to a target person as a list of (movie_id, person_id) pairs, or None if no path exists.

### Testing

A test script (`test_degrees.py`) has been developed to verify the correct operation of all listed functions.

### Technologies Used

- `Unittest`

### Usage

main: `python3 degrees.py small`
test: `python3 test_degrees.py`