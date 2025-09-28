import random

def simulate_martingale_strategy(starting_money, initial_bet, number_of_spins, roulette_variant):
    if roulette_variant == 'european':
        chance_of_red = 18/37
    elif roulette_variant == 'american':
        chance_of_red = 18/38
    else:
        chance_of_red = 18/37
    
    current_money = starting_money
    bet_amount = initial_bet
    total_wins = 0
    total_losses = 0
    
    for _ in range(number_of_spins):
        if current_money <= 0:
            break
            
        actual_bet = min(bet_amount, current_money)
        current_money -= actual_bet
        hit_red = random.random() < chance_of_red
        
        if hit_red:
            current_money += actual_bet * 2
            total_wins += 1
            bet_amount = initial_bet
        else:
            total_losses += 1
            bet_amount = actual_bet * 2
    
    return total_wins, total_losses, current_money


def run_interactive_simulation():
    try:
        starting_money = float(input("How much money to start with? (default: 1000): ") or 1000)
        initial_bet = float(input("What's your base bet amount? (default: 10): ") or 10) 
        number_of_spins = int(input("How many spins per simulation? (default: 1000): ") or 1000)
        roulette_variant = input("European or American roulette? (default: european): ").strip().lower() or "european"
        simulation_runs = int(input("How many simulations to run? (default: 1): ") or 1)
        
        if starting_money <= 0 or initial_bet <= 0 or number_of_spins <= 0:
            print("Please enter positive numbers only!")
            return
            
    except ValueError:
        print("Oops! Please enter valid numbers.")
        return
    
    all_results = []
    
    print(f"\n{'='*50}")
    print("SIMULATION RESULTS")
    print(f"{'='*50}")
    
    for run_number in range(1, simulation_runs + 1):
        wins, losses, final_money = simulate_martingale_strategy(
            starting_money, initial_bet, number_of_spins, roulette_variant
        )
        
        all_results.append((run_number, wins, losses, final_money))
        
        profit_loss = final_money - starting_money
        print(f"\nSimulation #{run_number}:")
        print(f"  Wins: {wins}")
        print(f"  Losses: {losses}")  
        print(f"  Final balance: ${final_money:.2f}")
        print(f"  Profit/Loss: ${profit_loss:.2f}")
    
    profitable_runs = [result for result in all_results if result[3] > starting_money]
    
    print(f"\n{'='*50}")
    print("OVERALL SUMMARY")
    print(f"{'='*50}")
    print(f"Profitable runs: {len(profitable_runs)} out of {simulation_runs}")
    print(f"Success rate: {(len(profitable_runs)/simulation_runs)*100:.1f}%")
    
    if profitable_ru_
