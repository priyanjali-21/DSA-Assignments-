from hash_table import *
import dynamic_hash_table as dht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
 

class MuskLibrary(DigitalLibrary):
    def __init__(self, book_titles, texts):
        self.lib = []
        for title, text in zip(book_titles, texts):
            # Sort words first to ensure consistent order
            sorted_words = self.merge_sort(text)
            distinct = []
            # Ensure we only add each word once
            for word in sorted_words:
                if not distinct or word != distinct[-1]:
                    distinct.append(word)
            self.lib.append((title, distinct))
        # Sort books by title for binary search
        self.lib = self.merge_sort(self.lib)
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def _find_book_idx(self, book_title):
        left, right = 0, len(self.lib) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.lib[mid][0] == book_title:
                return mid
            elif self.lib[mid][0] < book_title:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def distinct_words(self, book_title):
        idx = self._find_book_idx(book_title)
        if idx == -1:
            return []
        # Return a new list to avoid modifying the original
        return list(self.lib[idx][1])
    
    def count_distinct_words(self, book_title):
        idx = self._find_book_idx(book_title)
        return 0 if idx == -1 else len(self.lib[idx][1])
    
    def search_keyword(self, keyword):
        result = []
        for title, words in self.lib:
            left, right = 0, len(words) - 1
            while left <= right:
                mid = (left + right) // 2
                if words[mid] == keyword:
                    result.append(title)
                    break
                elif words[mid] < keyword:
                    left = mid + 1
                else:
                    right = mid - 1
        return result
    
    def print_books(self):
        for title, words in self.lib:
            words_str = " | ".join(words) if words else "⟨EMPTY⟩"
            print(f"{title}: {words_str}")


class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        self.name = name
        if name == "Jobs":
            collision_type = "Chain"
            self.params = (params[0], params[1])
        elif name == "Gates":
            collision_type = "Linear"
            self.params = (params[0], params[1])
        else:  # Bezos
            collision_type = "Double"
            self.params = params
            
        self.books = dht.DynamicHashMap(collision_type, self.params)  # book_title -> HashSet of words
        self.list_of_books = []

    def add_book(self, book_title, text):
        self.list_of_books.append(book_title)
        
        book_words = dht.DynamicHashSet(self.books.ct, self.params)  # Use DynamicHashSet
        for word in text:
            book_words.insert(word)  # Insert word into the HashSet for the book
        
        self.books.insert((book_title, book_words))  # Insert the book and its words
    
    def distinct_words(self, book_title):
        
        book = self.books.find(book_title)
        if book is None:
            return []
        
        words = []
        # Collect distinct words from the HashSet
        for i in range(book.table_size):
            if book.ct == "Chain":
                if book.table[i] is not None:
                    
                    for word, _ in book.table[i]:
                        words.append(word)
            
            else:  # Linear or Double hashing
                if book.table[i] is not None:
                    s = book.table[i][0]
                    words.append(s)
    
        return words
    
    
    def count_distinct_words(self, book_title):
        book = self.books.find(book_title)
        return 0 if book is None else book.num_elements
    
    
    def search_keyword(self, keyword):
        result_book_list = []
        for book in self.list_of_books:
            txt = self.books.find(book)

            if txt != None:
                keyword_exists = txt.find(keyword)

                if keyword_exists:
                    result_book_list.append(book)
        
        return result_book_list
        pass
    
    def print_books(self):
        for i in range(self.books.table_size):
            if self.books.table[i] is not None:
                if self.books.ct == "Chain":
                    for title, words in self.books.table[i]:
                        word_str = words.__str__()
                        print(f"{title}: {word_str}")
                else:
                    title, words = self.books.table[i]
                    word_str = words.__str__()
                    print(f"{title}: {word_str}")