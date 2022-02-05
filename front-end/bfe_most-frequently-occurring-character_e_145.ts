function count(str: string): string | string[] { // abbcccddd
    const mostFrequentChars: Record<string, number> = {}; // {a: 1, b: 2, c: 3, d: 3};
    let results: string[] = []; // [c, d]
    let maxFrequency = 0; // 3

    for (const char of str) {
        if(mostFrequentChars.hasOwnProperty(char)) {
            mostFrequentChars[char] += 1;
        } else {
            mostFrequentChars[char] = 1;
        }
    }

    Object.entries(mostFrequentChars).forEach(([char, frequency]) => {
        if (frequency > maxFrequency) {
            results = [char];
            maxFrequency = frequency
        } else if (frequency === maxFrequency) {
            results.push(char);
        }
    });

    return results.length === 1 ? results[0] : results;
}
