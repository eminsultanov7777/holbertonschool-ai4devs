// Fixed Bug 2: Boundary-condition logic error
// Users aged 18 or older can register.

function canRegister(age) {
    return age >= 18;
}

if (canRegister(18) !== true) throw new Error("Age 18 should be allowed");
if (canRegister(19) !== true) throw new Error("Age 19 should be allowed");
if (canRegister(17) !== false) throw new Error("Age 17 should not be allowed");

console.log("Bug 2 tests passed");
