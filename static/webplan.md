# Ignis Technologies Web Manual Testing Plan

## 1. Introduction

### Purpose
This document outlines the manual testing plan for the Ignis Technologies webpage (ignistech.io).

### Scope
This plan focuses on manual testing efforts, emphasizing end-to-end (E2E) testing and including some integration testing. It covers functional, UI, and non-functional aspects of the webpage.

Note: The current version of this plan does not include detailed test cases for the logged-in user area, as access to this section requires active credentials. These test cases will be added and expanded upon after completing the onboarding process.

## 2. Test Strategy

### 2.1 Testing Objectives
- Ensure the site meets all functional requirements
- Verify usability and user experience across industry standard browsers
- Validate integration of app components and third-party services
- Assess site performance under various conditions

### 2.2 Testing Types
- End-to-End (E2E) Testing
- Integration Testing
- User Interface (UI) Testing
- Functional Testing
- Non-Functional Testing

### 2.3 Testing Approach
- Manual testing as primary method
- Test cases derived from user stories and requirements
- Testing on industry standard browsers
- Critical path testing on every build
- Regression testing after major changes

### 2.4 Tools
- Will be filled in after I onboard and become familiar with toolset. 

## 3. Test Environment

### 3.1 Browsers
- 

### 3.2 Devices
- PC
- Tablet
- Mobile

## 4. Test Cases

### 4.1 Landing Page

#### 4.1.1 Header
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LP001 | Ignis Connect Link | Click on Ignis Connect link in header | User is directed to Ignis Connect page |
| LP002 | About Us Link | Click on About Us link in header | User is directed to About Us page |
| LP003 | Login Button | Click on Login button in header | User is directed to Login page |
| LP004 | Company Logo | Verify company logo presence and click | Logo is visible and clicks through to home page |

#### 4.1.2 Main Content
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LP005 | "Get Ignis Today!" CTA | Click on "Get Ignis Today!" button | Page scrolls down to subscription levels section |
| LP006 | "Connect to Ignis Now!" CTA | Click on "Connect to Ignis Now!" button | User is directed to Getting Started page (Create Account) |

#### 4.1.3 Subscription Levels
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LP007 | Ignis Lite Option | Click on Ignis Lite link | User is directed to App Store for Ignis Lite |
| LP008 | Ignis Core Option | Click on Ignis Core link | User is directed to App Store for Ignis Core |
| LP009 | Ignis Connect Option | Click on Ignis Connect link | User is directed to Getting Started page (Create Account) |

#### 4.1.4 Carousel
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LP010 | Newsletter Signup | Interact with newsletter signup option | User can sign up for newsletter |
| LP011 | Ignis Connect Link | Click on Ignis Connect link in carousel | User is directed to Ignis Connect page |
| LP012 | Social Media Links | Click on social media links in carousel | User is directed to respective social media pages |

#### 4.1.5 Footer
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LP013 | Social Links | Click on each social media link in footer | User is directed to respective social media pages |
| LP014 | Careers Link | Click on Careers link in footer | User is directed to Careers page |
| LP015 | Privacy Policy Link | Click on Privacy Policy link in footer | User is directed to Privacy Policy page |
| LP016 | Terms of Use Link | Click on Terms of Use link in footer | User is directed to Terms of Use page |

#### 4.1.6 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LP017 | Page Load | Open the landing page | Page loads completely without errors |
| LP018 | Responsive Design | View page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |

### 4.2 Login Page

#### 4.2.1 Login Form
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LG001 | Valid Login | 1. Enter valid username<br>2. Enter valid password<br>3. Click Login button | User is successfully logged in and directed to dashboard |
| LG002 | Invalid Username | 1. Enter invalid username<br>2. Enter valid password<br>3. Click Login button | Error message displayed, login denied |
| LG003 | Invalid Password | 1. Enter valid username<br>2. Enter invalid password<br>3. Click Login button | Error message displayed, login denied |
| LG004 | Empty Fields | Click Login button without entering credentials | Error message prompts user to enter credentials |

#### 4.2.2 Password Functionality
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LG005 | Reveal Password | 1. Enter password<br>2. Click reveal password button | Password becomes visible as plain text |
| LG006 | Hide Password | 1. Reveal password<br>2. Click hide password button | Password is hidden (displayed as asterisks) |

#### 4.2.3 Reset Password
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LG007 | Reset Password Link | Click on "Reset Password" link | User is directed to password reset page |

#### 4.2.4 Footer Links
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LG008 | Privacy Policy Link | Click on Privacy Policy link | User is directed to Privacy Policy page |
| LG009 | Terms of Use Link | Click on Terms of Use link | User is directed to Terms of Use page |
| LG010 | Contact Us Link | Click on Contact Us link | User is directed to Contact page or presented with contact information |

#### 4.2.5 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LG011 | Page Load | Navigate to login page | Login page loads completely without errors |
| LG012 | Responsive Design | View login page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |
| LG013 | Remember Me | 1. Check "Remember Me" box (if available)<br>2. Login<br>3. Close browser and reopen | User credentials are remembered on return visit |
| LG014 | Form Validation | Submit form with various invalid inputs (e.g., malformed email) | Appropriate error messages are displayed for each invalid input |

### 4.3 Sign Up Page

#### 4.3.1 Sign Up Form
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| SU001 | Valid Sign Up | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter valid Email Address<br>4. Enter valid Phone Number (optional)<br>5. Enter valid Org/Crew Name<br>6. Click Sign Up button | Account is created, user is directed to confirmation page or dashboard |
| SU002 | Empty Required Fields | Click Sign Up button without filling required fields | Error messages prompt user to fill required fields |
| SU003 | Invalid Email Format | Enter invalid email format and submit | Error message indicates invalid email format |
| SU004 | Optional Phone Number | 1. Complete form without phone number<br>2. Submit form | Form submits successfully without phone number |
| SU005 | Duplicate Email | Try to sign up with an email already in use | Error message indicates email is already registered |

#### 4.3.2 Form Validation
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| SU006 | First Name Validation | Enter various invalid inputs for First Name | Appropriate error messages are displayed |
| SU007 | Last Name Validation | Enter various invalid inputs for Last Name | Appropriate error messages are displayed |
| SU008 | Email Validation | Enter various invalid email formats | Appropriate error messages are displayed |
| SU009 | Phone Number Validation | Enter various invalid phone number formats | Appropriate error messages are displayed if entered |
| SU010 | Org/Crew Name Validation | Enter various invalid inputs for Org/Crew Name | Appropriate error messages are displayed |

#### 4.3.3 Terms and Privacy Links
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| SU011 | Terms of Use Link (Below Sign Up) | Click on Terms of Use link below Sign Up button | User is directed to Terms of Use page |
| SU012 | Privacy Policy Link (Below Sign Up) | Click on Privacy Policy link below Sign Up button | User is directed to Privacy Policy page |

#### 4.3.4 Footer Links
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| SU013 | Privacy Policy Link (Footer) | Click on Privacy Policy link in footer | User is directed to Privacy Policy page |
| SU014 | Terms of Use Link (Footer) | Click on Terms of Use link in footer | User is directed to Terms of Use page |
| SU015 | Contact Us Link (Footer) | Click on Contact Us link in footer | User is directed to Contact page or presented with contact information |

#### 4.3.5 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| SU016 | Page Load | Navigate to sign up page | Sign up page loads completely without errors |
| SU017 | Responsive Design | View sign up page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |
| SU018 | Form Reset | Click reset or clear form button (if available) | All form fields are cleared |
| SU019 | Successful Submission Feedback | Complete form correctly and submit | User receives clear confirmation of successful account creation |

### 4.4 Ignis Connect Page

#### 4.4.1 Header
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| IC001 | Logo | Click on the logo | User is directed to the home page |
| IC002 | Ignis Connect Link | Click on Ignis Connect link in header | Page refreshes or smoothly scrolls to top |
| IC003 | About Us Link | Click on About Us link in header | User is directed to About Us page |
| IC004 | Login Button | Click on Login button in header | User is directed to Login page |

#### 4.4.2 Main Content
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| IC005 | "Get Connect Now!" Button | Click on "Get Connect Now!" button | User is directed to the Sign Up page |
| IC006 | Checkout Help Link | Click on the link for help with checking out | User is directed to checkout help resources |
| IC007 | Sign Up Page Link/Button | Click on the additional Sign Up link/button | User is directed to the Sign Up page |
| IC008 | 31+ Seats Form Link | Click on the link for users interested in 31+ seats | User is directed to the appropriate form or section |

#### 4.4.3 Carousel
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| IC009 | Newsletter Signup | Interact with newsletter signup option in carousel | User can sign up for newsletter |
| IC010 | Ignis Connect Link in Carousel | Click on Ignis Connect link in carousel | Page refreshes or smoothly scrolls to top |
| IC011 | Social Media Links in Carousel | Click on social media links in carousel | User is directed to respective social media pages |

#### 4.4.4 Footer
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| IC012 | Social Links in Footer | Click on each social media link in footer | User is directed to respective social media pages |
| IC013 | Careers Link | Click on Careers link in footer | User is directed to Careers page |
| IC014 | Privacy Policy Link in Footer | Click on Privacy Policy link in footer | User is directed to Privacy Policy page |
| IC015 | Terms of Use Link in Footer | Click on Terms of Use link in footer | User is directed to Terms of Use page |

#### 4.4.5 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| IC016 | Page Load | Navigate to Ignis Connect page | Page loads completely without errors |
| IC017 | Responsive Design | View page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |
| IC018 | Content Accuracy | Review all text content on the page | All information is accurate and up-to-date |
| IC019 | Link Consistency | Check all links on the page | All links are consistent with their described destinations |

### 4.5 About Us Page

#### 4.5.1 Header
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| AU001 | Logo | Click on the logo | User is directed to the home page |
| AU002 | Ignis Connect Link | Click on Ignis Connect link in header | User is directed to Ignis Connect page |
| AU003 | About Us Link | Click on About Us link in header | Page refreshes or smoothly scrolls to top |
| AU004 | Login Button | Click on Login button in header | User is directed to Login page |

#### 4.5.2 Main Content
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| AU005 | Embedded Video | Play the embedded video | Video plays without issues, explaining the product/team |
| AU006 | Video Controls | Interact with video controls (play, pause, volume, etc.) | Video controls respond correctly |
| AU007 | Team Member Portraits | View team member portraits | All portraits load correctly and are clearly visible |
| AU008 | Portrait Information | Check information associated with each portrait | Accurate information is displayed for each team member |

#### 4.5.3 Contact Us Sign Up Form
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| AU009 | Form Submission | Fill out the contact form and submit | Form submits successfully, user receives confirmation |
| AU010 | Form Validation | Submit form with invalid or missing required fields | Appropriate error messages are displayed |
| AU011 | Email Field Validation | Enter invalid email format in the form | Error message indicates invalid email format |

#### 4.5.4 Carousel
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| AU012 | Newsletter Signup | Interact with newsletter signup option in carousel | User can sign up for newsletter |
| AU013 | Ignis Connect Link in Carousel | Click on Ignis Connect link in carousel | User is directed to Ignis Connect page |
| AU014 | Social Media Links in Carousel | Click on social media links in carousel | User is directed to respective social media pages |

#### 4.5.5 Footer
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| AU015 | Social Links in Footer | Click on each social media link in footer | User is directed to respective social media pages |
| AU016 | Careers Link | Click on Careers link in footer | User is directed to Careers page |
| AU017 | Privacy Policy Link in Footer | Click on Privacy Policy link in footer | User is directed to Privacy Policy page |
| AU018 | Terms of Use Link in Footer | Click on Terms of Use link in footer | User is directed to Terms of Use page |

#### 4.5.6 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| AU019 | Page Load | Navigate to About Us page | Page loads completely without errors |
| AU020 | Responsive Design | View page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |
| AU021 | Content Accuracy | Review all text content on the page | All information is accurate and up-to-date |
| AU022 | Image Loading | Check all images on the page | All images load correctly and are not distorted |

### 4.6 Careers Page

#### 4.6.1 Careers Form
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| CR001 | Valid Form Submission | 1. Enter valid email<br>2. Enter valid first name<br>3. Enter valid last name<br>4. Enter valid phone number<br>5. Upload cover letter<br>6. Upload resume<br>7. Complete reCaptcha<br>8. Click submit button | Form submits successfully, user receives confirmation |
| CR002 | Email Field Validation | Enter invalid email format | Error message indicates invalid email format |
| CR003 | First Name Validation | Leave first name field empty | Error message prompts user to enter first name |
| CR004 | Last Name Validation | Leave last name field empty | Error message prompts user to enter last name |
| CR005 | Phone Number Validation | Enter invalid phone number format | Error message indicates invalid phone number format |
| CR006 | Cover Letter Upload | Upload a cover letter file | File uploads successfully, file name displayed |
| CR007 | Resume Upload | Upload a resume file | File uploads successfully, file name displayed |
| CR008 | File Type Restriction | Attempt to upload non-permitted file type | Error message indicates invalid file type |
| CR009 | File Size Limit | Attempt to upload file exceeding size limit | Error message indicates file size exceeds limit |
| CR010 | reCaptcha Validation | Submit form without completing reCaptcha | Error message prompts user to complete reCaptcha |

#### 4.6.2 Form Submission
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| CR011 | Submit Button Functionality | Click submit button with all fields filled correctly | Form submits, user receives confirmation message |
| CR012 | Submit with Missing Required Fields | Submit form with one or more required fields empty | Error messages indicate which fields are required |

#### 4.6.3 reCaptcha Integration
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| CR013 | reCaptcha Display | Load the Careers page | reCaptcha widget is displayed correctly |
| CR014 | reCaptcha Interaction | Interact with reCaptcha widget | reCaptcha responds correctly to user interaction |
| CR015 | reCaptcha Completion | Complete reCaptcha challenge | reCaptcha indicates successful completion |

#### 4.6.4 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| CR016 | Page Load | Navigate to Careers page | Page loads completely without errors |
| CR017 | Responsive Design | View page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |
| CR018 | Form Reset | Click reset or clear form button (if available) | All form fields are cleared, uploaded file names removed |
| CR019 | Successful Submission Feedback | Complete form correctly and submit | User receives clear confirmation of successful submission |

### 4.7 Privacy Policy Page

#### 4.7.1 Header
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| PP001 | Logo | Click on the logo | User is directed to the home page |
| PP002 | Ignis Connect Link | Click on Ignis Connect link in header | User is directed to Ignis Connect page |
| PP003 | About Us Link | Click on About Us link in header | User is directed to About Us page |
| PP004 | Login Button | Click on Login button in header | User is directed to Login page |

#### 4.7.2 Main Content
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| PP005 | Privacy Policy Display | Navigate to Privacy Policy page | Privacy policy text is displayed correctly and fully |
| PP006 | Policy Readability | Scroll through the privacy policy | Text is legible and properly formatted |
| PP007 | Website Link | Click on the website link within the policy | User is directed to the main Ignis Technologies website |
| PP008 | Contact Email Link | Click on the "contact@ignistech.io" email link | Default email client opens with the address populated |

#### 4.7.3 Footer
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| PP009 | Social Links in Footer | Click on each social media link in footer | User is directed to respective social media pages |
| PP010 | Careers Link | Click on Careers link in footer | User is directed to Careers page |
| PP011 | Privacy Policy Link in Footer | Click on Privacy Policy link in footer | Page refreshes or smoothly scrolls to top |
| PP012 | Terms of Use Link in Footer | Click on Terms of Use link in footer | User is directed to Terms of Use page |

#### 4.7.4 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| PP013 | Page Load | Navigate to Privacy Policy page | Page loads completely without errors |
| PP014 | Responsive Design | View page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |
| PP015 | Content Accuracy | Review all text content on the page | All information is accurate and up-to-date |
| PP016 | Last Updated Date | Check for last updated date on the policy | Last updated date is visible and current |

### 4.8 Terms of Use Page

#### 4.8.1 Header
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| TU001 | Logo | Click on the logo | User is directed to the home page |
| TU002 | Ignis Connect Link | Click on Ignis Connect link in header | User is directed to Ignis Connect page |
| TU003 | About Us Link | Click on About Us link in header | User is directed to About Us page |
| TU004 | Login Button | Click on Login button in header | User is directed to Login page |

#### 4.8.2 Main Content
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| TU005 | Terms of Use Display | Navigate to Terms of Use page | Terms of Use text is displayed correctly and fully |
| TU006 | Terms Readability | Scroll through the Terms of Use | Text is legible and properly formatted |
| TU007 | Contact Email Link | Click on the "contact@ignistech.io" email link | Default email client opens with the address populated |

#### 4.8.3 Footer
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| TU008 | Social Links in Footer | Click on each social media link in footer | User is directed to respective social media pages |
| TU009 | Careers Link | Click on Careers link in footer | User is directed to Careers page |
| TU010 | Privacy Policy Link in Footer | Click on Privacy Policy link in footer | User is directed to Privacy Policy page |
| TU011 | Terms of Use Link in Footer | Click on Terms of Use link in footer | Page refreshes or smoothly scrolls to top |

#### 4.8.4 General
| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| TU012 | Page Load | Navigate to Terms of Use page | Page loads completely without errors |
| TU013 | Responsive Design | View page on different devices/screen sizes | Page layout adjusts appropriately for each screen size |
| TU014 | Content Accuracy | Review all text content on the page | All information is accurate and up-to-date |
| TU015 | Last Updated Date | Check for last updated date on the Terms | Last updated date is visible and current |
| TU016 | Sections and Headings | Review the structure of the Terms of Use | All sections and headings are clearly defined and navigable |

### 4.9 Logged-In User Area

Note: This section requires access to a user account and will be completed after onboarding.

| ID | Description | Steps | Expected Result |
|----|-------------|-------|-----------------|
| LU001 | Access Logged-In Area | Log in with valid credentials | User is directed to a dashboard or main logged-in page |
| LU002 | Placeholder | To be filled in after gaining access | To be determined |


## 5. Test Execution

### 5.1 Test Cycle
1. Smoke Testing
2. Functional Testing
3. UI/UX Testing
4. Integration Testing
5. Performance Testing
6. Regression Testing

### 5.2 Defect Management
- Log all defects in Jira or similar system
- Prioritize based on severity and impact
- Address critical defects immediately

### 5.3 Reporting
- Daily status updates during testing cycles
- Comprehensive test reports at cycle end

## 6. Risks and Mitigation

| Risk | Description | Mitigation Strategy |
|------|-------------|---------------------|
| Browser Compatibility | Website may not function correctly across all browsers | - Test on multiple browsers (Chrome, Firefox, Safari, Edge)<br>- Use browser emulators for less common browsers<br>- Implement cross-browser compatible code |
| Device Responsiveness | Layout issues on different screen sizes and devices | - Test on various devices (desktop, tablet, mobile)<br>- Use responsive design testing tools<br>- Implement and adhere to responsive design principles |
| Performance Issues | Slow loading times or poor performance on certain devices/networks | - Conduct performance testing using tools like Google PageSpeed Insights<br>- Optimize images and code<br>- Implement caching strategies |
| Security Vulnerabilities | Potential security risks in forms or data handling | - Conduct regular security audits<br>- Implement HTTPS across the site<br>- Use secure coding practices and input validation |
| Accessibility Compliance | Website may not meet accessibility standards | - Use accessibility testing tools (e.g., WAVE)<br>- Follow WCAG guidelines<br>- Conduct testing with screen readers |
| Content Accuracy | Outdated or incorrect information on the website | - Implement a content review process<br>- Regular content audits<br>- Clear process for content updates |
| Third-party Integrations | Issues with integrated services (e.g., reCaptcha, payment gateways) | - Regular testing of all integrations<br>- Maintain updated documentation on integrations<br>- Have fallback plans for critical integrations |
| Data Loss | Potential loss of user-submitted data | - Implement proper data backup strategies<br>- Use secure and reliable hosting services<br>- Regular database backups |
| User Experience Inconsistencies | Inconsistent UI/UX across different sections of the website | - Maintain a consistent design system<br>- Regular UX reviews<br>- User testing sessions |
| Load Handling | Website crash or slowdown during high traffic periods | - Conduct load testing<br>- Implement scalable infrastructure<br>- Have a content delivery network (CDN) in place |
| Broken Links | Dead links leading to 404 errors | - Regular link checking using automated tools<br>- Implement proper redirects<br>- Regular content audits |
| Cookie and Privacy Compliance | Non-compliance with cookie laws and privacy regulations | - Implement proper cookie consent mechanisms<br>- Regular review of privacy policy and terms<br>- Stay updated with latest privacy regulations |



