document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const togglePasswordBtn = document.getElementById("togglePassword");
  
    // Password Visibility Toggle
    togglePasswordBtn.addEventListener("click", () => {
      const type =
        passwordInput.getAttribute("type") === "password" ? "text" : "password";
      passwordInput.setAttribute("type", type);
  
      // Toggle Icon
      const icon = togglePasswordBtn.querySelector("i");
      icon.classList.toggle("bi-eye");
      icon.classList.toggle("bi-eye-slash");
    });
  
    // Dummy Validation Logic
   /* const validateEmail = (email) => {
      return String(email)
        .toLowerCase()
        .match(
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
    };
  
    const showError = (input, errorId, show) => {
      const errorElement = document.getElementById(errorId);
      if (show) {
        input.classList.add("invalid");
        errorElement.style.display = "block";
      } else {
        input.classList.remove("invalid");
        errorElement.style.display = "none";
      }
    };
  
    // Real-time validation cleanup on typing
    emailInput.addEventListener("input", () => {
      if (emailInput.classList.contains("invalid")) {
        showError(emailInput, "emailError", false);
      }
    });
  
    passwordInput.addEventListener("input", () => {
      if (passwordInput.classList.contains("invalid")) {
        showError(passwordInput, "passwordError", false);
      }
    });*/
  
    // Form Submit
    loginForm.addEventListener("submit", (e) => {
        //e.preventDefault();
        let isValid = true;
    
        /* removing client side validation
        // Email check
        if (!validateEmail(emailInput.value)) {
            showError(emailInput, "emailError", true);
            isValid = false;
        }
    
        // Password check
        if (passwordInput.value.length < 6) {
            showError(passwordInput, "passwordError", true);
            isValid = false;
        }
            */

        if (!isValid) {
            e.preventDefault();
            return;
        }

        const btn = loginForm.querySelector(".btn-login");
        btn.disabled = true;
        btn.innerText = "Signing in...";
  
        /* if (isValid) {
            // Simulating successful login
            const btn = loginForm.querySelector(".btn-login");
            const originalText = btn.innerText;
            btn.disabled = true;
            btn.innerText = "Signing in...";
    
            setTimeout(() => {
            console.log("Login attempt successful with:", {
                email: emailInput.value,
                password: passwordInput.value
            });
            btn.innerText = "Success!";
            btn.style.backgroundColor = "#10b981"; // Success Green
    
            setTimeout(() => {
                btn.disabled = false;
                btn.innerText = originalText;
                btn.style.backgroundColor = "";
            }, 2000);
            }, 1500);
        } */
    });
  });
  