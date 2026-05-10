universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    enrollments = []
    tuitions = []
    for university in data:
        enrollments.append(university[1])
        tuitions.append(university[2])
    return enrollments, tuitions

def mean(values):
    a = f"{sum(values)/len(values):.2f}"
    return a
def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1]+sorted_values[mid])/2
    else:
        return sorted_values[mid]
enrollments, tuitions = enrollment_stats(universities)


total_students = sum(enrollments)
total_tuitions = sum(tuitions)

student_mean = mean(enrollments)
student_median = median(enrollments)

tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

print("*"*40)
print(f"Total students: {total_students}")
print(f"Total tuition: {total_tuitions}\n")

print(f"Student mean: {student_mean}")
print(f"Student median: {student_median}\n")

print(f"Tuition mean: {tuition_mean}")
print(f"Tuition meadian: {tuition_median}\n")
print("*"*40)




