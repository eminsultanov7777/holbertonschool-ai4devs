// Bug 2: Logical error
// Intended behavior: Return true when a user is old enough to register (18+).

function canRegister(age) {
    if (age > 18) {
        return true;
    }
    return false;
}

const testAges = [16, 17, 18, 19, 25];

for (const age of testAges) {
    console.log(`Age ${age}:`, canRegister(age));
}

// Expected: age 18 and above should return true.
// Actual: age 18 incorrectly returns false.
