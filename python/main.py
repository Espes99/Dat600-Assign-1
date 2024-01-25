from plot_generator import generate_sort_algorithm_plot
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

def main():
    #generate_sort_algorithm_plot(heap_sort, "O(N log N)")
    #generate_sort_algorithm_plot(insertion_sort, "O(N^2)")
    #generate_sort_algorithm_plot(merge_sort, "O(N log N)")
    generate_sort_algorithm_plot(quick_sort, "O(N log N)")
if __name__ == "__main__":
    main()