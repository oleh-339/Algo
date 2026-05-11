import os

def find_longest_chain(words: list) -> int:
    if not words:
        return 0

    chains = {}
    max_total_length = 1

    words.sort(key=len)

    for word in words:
        best_previous_chain = 1
        
        for i in range(len(word)):
            shorter_word = word[:i] + word[i + 1:]
            
            if shorter_word in chains:
                if chains[shorter_word] + 1 > best_previous_chain:
                    best_previous_chain = chains[shorter_word] + 1
                
        chains[word] = best_previous_chain
        
        if best_previous_chain > max_total_length:
            max_total_length = best_previous_chain

    return max_total_length

def main():
    input_path = 'wchain.in'
    output_path = 'wchain.out'

    if not os.path.exists(input_path):
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.read().split()
        
    if not lines:
        return
        
    word_list = lines[1:] 
    
    result = find_longest_chain(word_list)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(result) + '\n')

if __name__ == "__main__":
    main()
