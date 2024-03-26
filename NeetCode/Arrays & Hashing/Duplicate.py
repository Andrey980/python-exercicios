def verificaDuplicata(numeros):

    numeros_unicos = set()

    for num in numeros:
        if num in numeros_unicos:
            return True
        else:
            numeros_unicos.add(num)

    return False


nums1 = [1, 2, 3, 1]
print(verificaDuplicata(nums1))

nums2 = [1, 2, 3, 4]
print(verificaDuplicata(nums2))

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(verificaDuplicata(nums3))
