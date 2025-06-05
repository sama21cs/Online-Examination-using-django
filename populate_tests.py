from django.contrib.auth.models import User
from examapp.models import Test, Question

def populate_tests():
    # DSA Test data
    test_data = {
        "title": "DSA Test",
        "duration": 60,
        "total_questions": 45,
        "total_marks": 45,
        "negative_marks": False,
        "sections": 1
    }

    # 45 Questions for DSA Test
    questions_data = [
        {"text": "What is the time complexity of binary search?", "option1": "O(n)", "option2": "O(log n)", "option3": "O(n^2)", "option4": "O(1)", "correct_answer": "O(log n)", "marks": 1},
        {"text": "Which data structure is used in a queue?", "option1": "Array", "option2": "Linked List", "option3": "Both", "option4": "None", "correct_answer": "Both", "marks": 1},
        {"text": "What is the best case time complexity of QuickSort?", "option1": "O(n)", "option2": "O(n log n)", "option3": "O(n^2)", "option4": "O(log n)", "correct_answer": "O(n log n)", "marks": 1},
        {"text": "Which algorithm finds the shortest path in a weighted graph?", "option1": "BFS", "option2": "DFS", "option3": "Dijkstra's", "option4": "Kruskal's", "correct_answer": "Dijkstra's", "marks": 1},
        {"text": "What is a stack primarily used for?", "option1": "Sorting", "option2": "Searching", "option3": "LIFO operations", "option4": "FIFO operations", "correct_answer": "LIFO operations", "marks": 1},
        {"text": "Which sorting algorithm is stable?", "option1": "QuickSort", "option2": "HeapSort", "option3": "MergeSort", "option4": "SelectionSort", "correct_answer": "MergeSort", "marks": 1},
        {"text": "What is the space complexity of a binary tree traversal?", "option1": "O(1)", "option2": "O(n)", "option3": "O(log n)", "option4": "O(n^2)", "correct_answer": "O(n)", "marks": 1},
        {"text": "Which data structure uses a hash function?", "option1": "Stack", "option2": "Queue", "option3": "HashMap", "option4": "Tree", "correct_answer": "HashMap", "marks": 1},
        {"text": "What is dynamic programming used for?", "option1": "Sorting", "option2": "Optimization", "option3": "Searching", "option4": "Graph traversal", "correct_answer": "Optimization", "marks": 1},
        {"text": "Which algorithm is used for minimum spanning tree?", "option1": "Dijkstra's", "option2": "Prim's", "option3": "Bellman-Ford", "option4": "Floyd-Warshall", "correct_answer": "Prim's", "marks": 1},
        {"text": "What is the worst-case time complexity of linear search?", "option1": "O(1)", "option2": "O(log n)", "option3": "O(n)", "option4": "O(n^2)", "correct_answer": "O(n)", "marks": 1},
        {"text": "Which traversal method uses recursion heavily?", "option1": "Inorder", "option2": "Preorder", "option3": "Postorder", "option4": "All of the above", "correct_answer": "All of the above", "marks": 1},
        {"text": "In a max heap, which node has the highest value?", "option1": "Leaf Node", "option2": "Root Node", "option3": "Right Child", "option4": "Left Child", "correct_answer": "Root Node", "marks": 1},
        {"text": "Which data structure is used for function call management in recursion?", "option1": "Queue", "option2": "Stack", "option3": "Heap", "option4": "Tree", "correct_answer": "Stack", "marks": 1},
        {"text": "Which sorting algorithm has the best average-case performance?", "option1": "Selection Sort", "option2": "Bubble Sort", "option3": "MergeSort", "option4": "Insertion Sort", "correct_answer": "MergeSort", "marks": 1},
        {"text": "What is the time complexity of inserting into a Binary Search Tree (average case)?", "option1": "O(log n)", "option2": "O(n)", "option3": "O(n log n)", "option4": "O(1)", "correct_answer": "O(log n)", "marks": 1},
        {"text": "Which traversal of a binary search tree gives sorted output?", "option1": "Preorder", "option2": "Postorder", "option3": "Inorder", "option4": "Level order", "correct_answer": "Inorder", "marks": 1},
        {"text": "Which graph traversal algorithm uses a queue?", "option1": "DFS", "option2": "BFS", "option3": "Dijkstra", "option4": "Kruskal", "correct_answer": "BFS", "marks": 1},
        {"text": "Which of the following is not a self-balancing BST?", "option1": "AVL", "option2": "Red-Black Tree", "option3": "Binary Heap", "option4": "Splay Tree", "correct_answer": "Binary Heap", "marks": 1},
        {"text": "Which algorithm is best for cycle detection in a graph?", "option1": "DFS", "option2": "BFS", "option3": "Kruskal's", "option4": "Dijkstra's", "correct_answer": "DFS", "marks": 1},
        {"text": "What is the auxiliary space complexity of Merge Sort?", "option1": "O(1)", "option2": "O(log n)", "option3": "O(n)", "option4": "O(n^2)", "correct_answer": "O(n)", "marks": 1},
        {"text": "Which data structure provides constant time complexity for insertion and search?", "option1": "Array", "option2": "Linked List", "option3": "HashMap", "option4": "Binary Tree", "correct_answer": "HashMap", "marks": 1},
        {"text": "Which graph algorithm can be used to detect negative weight cycles?", "option1": "Kruskal", "option2": "Bellman-Ford", "option3": "Prim", "option4": "Dijkstra", "correct_answer": "Bellman-Ford", "marks": 1},
        {"text": "Which is not a characteristic of greedy algorithms?", "option1": "Optimal Substructure", "option2": "Overlapping Subproblems", "option3": "Greedy Choice Property", "option4": "None", "correct_answer": "Overlapping Subproblems", "marks": 1},
        {"text": "Which sorting algorithm is in-place and unstable?", "option1": "QuickSort", "option2": "MergeSort", "option3": "Bubble Sort", "option4": "Insertion Sort", "correct_answer": "QuickSort", "marks": 1},
        {"text": "What is the key idea behind dynamic programming?", "option1": "Divide and Conquer", "option2": "Memoization", "option3": "Backtracking", "option4": "Greedy Selection", "correct_answer": "Memoization", "marks": 1},
        {"text": "What does BFS stand for?", "option1": "Best First Search", "option2": "Breadth First Search", "option3": "Binary First Search", "option4": "Backwards First Search", "correct_answer": "Breadth First Search", "marks": 1},
        {"text": "What is the number of edges in a complete graph with n vertices?", "option1": "n", "option2": "n(n-1)", "option3": "n(n-1)/2", "option4": "2n", "correct_answer": "n(n-1)/2", "marks": 1},
        {"text": "Which of the following is a non-linear data structure?", "option1": "Array", "option2": "Linked List", "option3": "Stack", "option4": "Tree", "correct_answer": "Tree", "marks": 1},
        {"text": "What is the primary use of a priority queue?", "option1": "Fast access", "option2": "LIFO access", "option3": "Sorted order access", "option4": "Access highest priority element", "correct_answer": "Access highest priority element", "marks": 1},
        {"text": "What is the time complexity of heapify?", "option1": "O(log n)", "option2": "O(n)", "option3": "O(n log n)", "option4": "O(1)", "correct_answer": "O(log n)", "marks": 1},
        {"text": "What is the maximum number of nodes in a binary tree of height h?", "option1": "2^h", "option2": "2^(h+1)-1", "option3": "h", "option4": "h^2", "correct_answer": "2^(h+1)-1", "marks": 1},
        {"text": "Which traversal is used in topological sorting?", "option1": "Preorder", "option2": "DFS", "option3": "BFS", "option4": "Inorder", "correct_answer": "DFS", "marks": 1},
        {"text": "Which tree traversal is used for expression trees?", "option1": "Inorder", "option2": "Postorder", "option3": "Preorder", "option4": "Level order", "correct_answer": "Postorder", "marks": 1},
        {"text": "What does a binary search require?", "option1": "Sorted data", "option2": "Unsorted data", "option3": "Hash table", "option4": "Heap", "correct_answer": "Sorted data", "marks": 1},
        {"text": "Which algorithm is used for All-Pairs Shortest Path?", "option1": "Dijkstra", "option2": "Floyd-Warshall", "option3": "Prim", "option4": "Kruskal", "correct_answer": "Floyd-Warshall", "marks": 1},
        {"text": "Which is a divide and conquer algorithm?", "option1": "Merge Sort", "option2": "Bubble Sort", "option3": "Insertion Sort", "option4": "Selection Sort", "correct_answer": "Merge Sort", "marks": 1},
        {"text": "Which data structure supports constant time insertion and deletion at both ends?", "option1": "Deque", "option2": "Queue", "option3": "Stack", "option4": "Array", "correct_answer": "Deque", "marks": 1},
        {"text": "Which tree does not allow duplicates?", "option1": "Binary Tree", "option2": "Binary Search Tree", "option3": "AVL Tree", "option4": "Heap", "correct_answer": "Binary Search Tree", "marks": 1},
        {"text": "Which of these is not a characteristic of a heap?", "option1": "Complete binary tree", "option2": "Heap order property", "option3": "Balanced", "option4": "Sorted order", "correct_answer": "Sorted order", "marks": 1},
        {"text": "Which of the following is used in backtracking?", "option1": "Recursion", "option2": "Stack", "option3": "Queue", "option4": "Greedy approach", "correct_answer": "Recursion", "marks": 1},
        {"text": "Which graph algorithm can handle disconnected components?", "option1": "Prim's", "option2": "Kruskal's", "option3": "Dijkstra's", "option4": "BFS", "correct_answer": "Kruskal's", "marks": 1},
        {"text": "Which hashing method handles collisions?", "option1": "Separate chaining", "option2": "Open addressing", "option3": "Both", "option4": "None", "correct_answer": "Both", "marks": 1},
        {"text": "What is a key drawback of linear probing in hashing?", "option1": "Requires more memory", "option2": "Slower lookups", "option3": "Clustering", "option4": "Does not resolve collisions", "correct_answer": "Clustering", "marks": 1},
        {"text": "Which algorithm is used for finding connected components in a graph?", "option1": "DFS", "option2": "Prim's", "option3": "Kruskal's", "option4": "Dijkstra's", "correct_answer": "DFS", "marks": 1},
    ]

    # Create or update DSA Test
    test, created = Test.objects.get_or_create(
        title=test_data["title"],
        defaults={
            "duration": test_data["duration"],
            "total_questions": test_data["total_questions"],
            "total_marks": test_data["total_marks"],
            "negative_marks": test_data["negative_marks"],
            "sections": test_data["sections"],
        }
    )
    if created:
        print(f"Created test: {test.title}")
    else:
        print(f"Test already exists: {test.title}")
        test.duration = test_data["duration"]
        test.total_questions = test_data["total_questions"]
        test.total_marks = test_data["total_marks"]
        test.negative_marks = test_data["negative_marks"]
        test.sections = test_data["sections"]
        test.save()

    # Add questions for the test
    Question.objects.filter(test=test).delete()  # Clear existing questions to avoid duplicates
    for question_data in questions_data:
        Question.objects.create(
            test=test,
            text=question_data["text"],
            is_mcq=True,
            option1=question_data["option1"],
            option2=question_data["option2"],
            option3=question_data["option3"],
            option4=question_data["option4"],
            correct_answer=question_data["correct_answer"],
            marks=question_data["marks"],
        )
        print(f"Added question: {question_data['text'][:50]}... for {test.title}")

if __name__ == "__main__":
    populate_tests()