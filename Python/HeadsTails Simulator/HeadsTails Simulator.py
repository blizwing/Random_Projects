import numpy as np


def simulate_coin_flip_tournament(num_participants=1000):
    # Initialize variables
    num_rounds = 0
    current_round_size = num_participants
    previous_round_flips = None  # To store flips from the previous round

    while current_round_size > 1:
        # Simulate coin flips
        flips = np.random.choice(['heads', 'tails'], size=current_round_size)

        # Eliminate tails and move heads to the next round
        current_round_size = np.sum(flips == 'heads')

        # Increment rounds
        num_rounds += 1

        # Check for same result situation
        if np.all(flips == 'heads') or np.all(flips == 'tails'):
            print(f"Round {num_rounds} invalidated due to all participants getting the same result.")
            continue

        # Store flips from the current round
        previous_round_flips = flips.copy()

        # Display results for the current round
        print(f"Round {num_rounds}: {current_round_size} participants")

    # Final winner
    print(f"\nFinal Winner: {current_round_size} participants remaining.")
    print(f"Total Rounds: {num_rounds}")
    print(f"Number of Heads Flipped by Final Winner: {np.sum(previous_round_flips == 'heads').item()}")


# Run the simulation
simulate_coin_flip_tournament()
