"""
Created by Sarmad Syed 11/12/16
"""

import re
import sys


def clean(text):
    text = re.sub('\[^a-zA-Z]\s','', text)
    text = re.sub(' w+', ' ', text)

    text = text.strip('\t\n\r')
    return text
s = []
for i in s:
    i.index()
def compare(text):
    original_parts = text.split('|')
    clean_parts = [clean(x) for x in original_parts]
    original_parts_to_check = []
    ignore_idx = []
    for idx, ele in enumerate(original_parts):
        if idx in ignore_idx:

            continue
        # The case of alphabetic characters should be ignored
        if len(ele) < 2:
            continue
        # Duplicates must also be filtered -if two passages are considered equal with respect to the comparison rules listed above, only the shortest should be retained.
        if clean_parts[idx] in clean_parts[:idx] + clean_parts[idx + 1:]:
            indices = [i for i, x in enumerate(clean_parts) if x == clean_parts[idx]]
            use = indices[0]
            for i in indices[1:]:
                if len(original_parts[i]) < len(original_parts[use]):
                    use = i
            if idx == use:
                ignore_idx += indices
            else:
                ignore_idx += [x for x in indices if x != use]
                continue
        original_parts_to_check.append(idx)
    # Doing the text in text matching here. Depending on size and type of dataset,
    # Which you should test as it would affect this, you may want this as part
    # of the function above, or before, etc. If you're only doing 100 bits of
    # data, then it doesn't matter. Optimize accordingly.
    text_to_return = []
    clean_to_check = [clean_parts[x] for x in original_parts_to_check]
    for idx in original_parts_to_check:
        # This bit can be done better, but I have no more time to work on this.
        if any([(clean_parts[idx] in clean_text) for clean_text in
                [x for x in clean_to_check if x != clean_parts[idx]]]):
            continue
        text_to_return.append(original_parts[idx])
    # The retained passages should be output in their original form (identical to the input passage), and in the same order.
    return '|'.join(text_to_return)

with open(sys.argv[1]) as file:
    for line in file:
        print compare(line)
