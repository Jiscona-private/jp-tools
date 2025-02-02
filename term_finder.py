print("Welcome to JP's term finder!")
fileName = input("Enter the name of the file that is searched: ")
searchTerm = input("Enter the term that is searched for: ")

def count_occurrences_in_chunks(file_path, search_term, chunk_size=1024*1024):
    count = 0
    leftover = ""
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        while chunk := file.read(chunk_size):  # Read file in chunks
            chunk = leftover + chunk  # Include leftover from previous read
            count += chunk.count(search_term)
            leftover = chunk[-len(search_term):]  # Keep possible split word
    
    return count

# Example usage
result = count_occurrences_in_chunks(fileName, searchTerm)
print(f"Occurrences of '{searchTerm}': {result}")
input("Press enter to leave.")
