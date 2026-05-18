import os


def bucket_sort_by_len(words: list) -> list:
    buckets = [[] for _ in range(51)]
    
    for word in words:
        length = len(word)
        if length <= 50:
            buckets[length].append(word)
            
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(bucket)
    return sorted_list


def find_longest_chain(words: list) -> int:
    if not words:
        return 0

    sorted_words = bucket_sort_by_len(words)
    
    chains = {}
    max_total_length = 1

    for word in sorted_words:
        best_previous_chain = 1
        
        for i in range(len(word)):
            shorter_word = word[:i] + word[i + 1:]
            
            if shorter_word in chains:
                best_previous_chain = max(best_previous_chain, chains[shorter_word] + 1)
                
        chains[word] = best_previous_chain
        max_total_length = max(max_total_length, best_previous_chain)

    return max_total_length


def main():
    input_path = 'wchain.in'
    output_path = 'wchain.out'

    if not os.path.exists(input_path):
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read().split()
        
    if not data:
        return
        
    word_list = data[1:] 
    
    result = find_longest_chain(word_list)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(result) + '\n')


if __name__ == "__main__":
    main()