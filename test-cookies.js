// Complete Netflix Cookie Validator Script

function validateNetflixCookie(cookie) {
    const cookiePattern = /__Secure-nlbi[=|;].*\bNetflixSession\b.*;/;
    const isValid = cookiePattern.test(cookie);

    if (isValid) {
        return "This cookie is valid for Netflix.";
    } else {
        return "This cookie is invalid for Netflix.";
    }
}

// Example usage
const cookie = "__Secure-nlbi=YOUR_COOKIE_VALUE; NetflixSession=YOUR_SESSION_VALUE;";
console.log(validateNetflixCookie(cookie));