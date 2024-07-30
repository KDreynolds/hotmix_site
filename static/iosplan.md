# Ignis Technologies iOS Manual Testing Plan

## 1. Introduction

### Purpose
This document outlines the manual testing plan for the Ignis Technologies iOS mobile application.

### Scope
This plan focuses on manual testing efforts, emphasizing end-to-end (E2E) testing and including some integration testing. It covers functional, UI, and non-functional aspects of the app.

## 2. Test Strategy

### 2.1 Testing Objectives
- Ensure the app meets all functional requirements
- Verify usability and user experience across iOS devices
- Validate integration of app components and third-party services
- Assess app performance under various conditions

### 2.2 Testing Types
- End-to-End (E2E) Testing
- Integration Testing
- User Interface (UI) Testing
- Functional Testing
- Non-Functional Testing

### 2.3 Testing Approach
- Manual testing as primary method
- Test cases derived from user stories and requirements
- Testing on actual iOS devices (if possible:various models and OS versions, I currently have an iPhone 14 running iOS 17.5.1)
- Critical path testing on every build
- Regression testing after major changes

### 2.4 Tools
- Will be filled in after I onboard and become familiar with toolset. 

## 3. Test Environment

### 3.1 Devices
- iPhone 14 (iOS 17.5.1)

### 3.2 iOS Versions
- iOS 17.5.1

## 4. Test Cases

### 4.1 Login Page

| ID    | Description                | Steps                                                                                 | Expected Result                                    |
|-------|----------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------|
| LC001 | User Registration          | 1. Open app<br>2. Tap "Register"<br>3. Fill in details (name, email, password)<br>4. Submit | Account created successfully, user logged in |
| LC002 | User Login - Valid         | 1. Enter valid email and password<br>2. Tap login                                     | User logged in, main map screen displayed           |
| LC003 | User Login - Invalid       | 1. Enter invalid email or password<br>2. Tap login                                    | Error message displayed, login denied               |
| LC004 | Face ID Login              | 1. Enable Face ID in settings<br>2. Log out<br>3. Attempt to log in using Face ID    | Face ID recognized, user logged in successfully     |
| LC005 | Forgot Password Flow       | 1. Tap "Forgot Password"<br>2. Enter email<br>3. Tap submit<br>4. Check email<br>5. Follow reset link<br>6. Set new password | Password reset email received, able to set new password |
| LC006 | Password Reveal Option     | 1. Enter password<br>2. Tap eye icon to reveal password<br>3. Tap again to hide      | Password visibility toggles correctly               |
| LC007 | Remember Me - Enable       | 1. Enter credentials<br>2. Check "Remember Me"<br>3. Log in<br>4. Close app<br>5. Reopen app | App opens to logged-in state                        |
| LC008 | Remember Me - Disable      | 1. Enter credentials<br>2. Uncheck "Remember Me"<br>3. Log in<br>4. Close app<br>5. Reopen app | App opens to login page                             |
| LC009 | Email Field Validation     | 1. Enter invalid email format<br>2. Tap login                                         | Error message for invalid email format              |
| LC010 | Password Strength Check    | 1. During registration, enter weak password<br>2. Observe feedback                   | Password strength indicator shown, suggestions given|
| LC011 | Login Button State         | 1. Leave email/password fields empty<br>2. Fill in both fields                       | Login button disabled when fields empty, enabled when filled |
| LC012 | Keyboard Functionality     | 1. Tap email field<br>2. Verify keyboard type<br>3. Tap password field<br>4. Verify keyboard type | Email keyboard for email, secure entry for password |
| LC013 | Logout Functionality       | 1. Log in to the app<br>2. Navigate to settings<br>3. Tap logout                     | User logged out, returned to login page             |

### 4.2 Map Screen

| ID    | Description                    | Steps                                                                                 | Expected Result                                         |
|-------|--------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------|
| MS001 | Basic Map Navigation           | 1. Zoom in/out on map<br>2. Pan across map<br>3. Observe map response                | Map zooms and pans smoothly, details update accordingly |
| MS002 | Wildfire Marker Interaction    | 1. Tap on a wildfire marker<br>2. Observe information display                         | Wildfire info popup appears with correct information    |
| MS003 | Wildfire Information Update    | 1. View map<br>2. Wait for set period (e.g., 5 mins)<br>3. Check for updates          | Map updates with latest wildfire information             |
| MS004 | Verify Wildfire Information    | 1. Select a wildfire<br>2. View detailed information<br>3. Cross-check with official sources | Displayed information matches official data             |
| MS005 | Copy Fire Coordinates          | 1. Select a wildfire<br>2. Locate coordinate information<br>3. Use copy function      | Coordinates copied to clipboard correctly               |
| MS006 | 3D Map View                    | 1. Enable 3D view option<br>2. Navigate map in 3D<br>3. Select a wildfire             | 3D view renders correctly, wildfire info accessible     |
| MS007 | Zoom to Location               | 1. Use "Zoom to Location" feature<br>2. Enter or select a location<br>3. Observe map  | Map centers and zooms to the specified location         |
| MS008 | Current Location               | 1. Tap "Current Location" button<br>2. Allow location access if prompted              | Map centers on user's current location                  |
| MS009 | Offline Map Functionality      | 1. Download offline map for an area<br>2. Enable airplane mode<br>3. Navigate map     | Offline map accessible and functional without internet  |
| MS010 | Map Legend                     | 1. Open map legend<br>2. Verify all symbols and colors                                | Legend accurately represents all map elements           |


### 4.3 Sidebar Menu

#### 4.3.1 Profile

| ID    | Description           | Steps                                                              | Expected Result                                    |
|-------|-----------------------|--------------------------------------------------------------------|-----------------------------------------------------|
| PR001 | Enter First Name      | 1. Open Profile<br>2. Enter/Edit First Name<br>3. Save changes     | First name updated successfully                     |
| PR002 | Enter Last Name       | 1. Open Profile<br>2. Enter/Edit Last Name<br>3. Save changes      | Last name updated successfully                      |
| PR003 | Enter Email           | 1. Open Profile<br>2. Enter/Edit Email<br>3. Save changes          | Email updated successfully                          |
| PR004 | Save Profile Changes  | 1. Make changes to profile<br>2. Tap Save button                   | All changes saved, confirmation message displayed   |
| PR005 | Delete Account        | 1. Tap Delete Account button<br>2. Confirm deletion                | Account deleted, user logged out                    |

#### 4.3.2 Reference Documents

| ID    | Description                    | Steps                                                              | Expected Result                                    |
|-------|--------------------------------|--------------------------------------------------------------------|-----------------------------------------------------|
| RD001 | Access Fire Weather Forecast   | Tap Fire Weather Forecast button                                   | Fire weather forecast information displayed         |
| RD002 | Access SIT Report              | Tap SIT Report button                                              | SIT Report displayed or downloaded                  |
| RD003 | Toggle Documents and Links     | Tap Documents and Links toggle                                     | View switches between Documents and Links sections  |

##### Documents Section

| ID    | Description                    | Steps                                                              | Expected Result                                    |
|-------|--------------------------------|--------------------------------------------------------------------|-----------------------------------------------------|
| RD004 | Expand NWCG Section            | Tap NWCG expandable section                                        | NWCG subsections become visible                     |
| RD005 | Access Five Steps to a Safe Flight | Tap "Five Steps to a Safe Flight (Orange Card)"                | Document opens correctly                            |
| RD006 | Access Standard for Helicopter Operations | Tap "Standard for Helicopter Operations"                | Document opens correctly                            |
| RD007 | Access Interagency Red Book    | Tap "Interagency Red Book"                                         | Document opens correctly                            |
| RD008 | Access NWCG Standards for Aviation Transport | Tap "NWCG Standards for Aviation Transport"          | Document opens correctly                            |
| RD009 | Expand 8 Line Medical Section  | Tap 8 Line Medical expandable section                              | 8 Line Medical subsections become visible           |
| RD010 | Access Medical Plan            | Tap "Medical Plan (ICS 206 WF)"                                    | Document opens correctly                            |
| RD011 | Expand CTR Section             | Tap CTR expandable section                                         | CTR subsections become visible                      |
| RD012 | Access Crew Time Report        | Tap "Crew Time Report"                                             | Document opens correctly                            |
| RD013 | Expand IRPG Section            | Tap IRPG expandable section                                        | IRPG subsections become visible                     |
| RD014 | Access NWCG IRPG               | Tap "NWCG IRPG"                                                    | Document opens correctly                            |
| RD015 | Expand Helicopter Passenger Briefing | Tap Helicopter Passenger Briefing expandable section         | Subsections become visible                          |
| RD016 | Access Helicopter Passenger Briefing | Tap "Helicopter Passenger Briefing"                          | Document opens correctly                            |

##### Links Section

| ID    | Description                    | Steps                                                              | Expected Result                                    |
|-------|--------------------------------|--------------------------------------------------------------------|-----------------------------------------------------|
| RD017 | Access InciWeb                 | Tap InciWeb link                                                   | InciWeb website opens in browser or in-app          |
| RD018 | Access NICC                    | Tap NICC link                                                      | NICC website opens in browser or in-app             |
| RD019 | Access NWS - Fire              | Tap NWS - Fire link                                                | NWS Fire website opens in browser or in-app         |

#### 4.3.3 Settings

| ID    | Description                  | Steps                                                        | Expected Result                                    |
|-------|------------------------------|--------------------------------------------------------------|-----------------------------------------------------|
| ST001 | Color Blind Mode Toggle      | 1. Open Settings<br>2. Toggle Color Blind Mode               | App display adjusts for color blind accessibility   |
| ST002 | Clear Map Caches on Launch   | 1. Open Settings<br>2. Toggle Clear Map Caches               | Map caches cleared on next app launch               |

#### 4.3.3 Feedback and Support

| ID    | Description                  | Steps                                                        | Expected Result                                    |
|-------|------------------------------|--------------------------------------------------------------|-----------------------------------------------------|
| FS001 | Application Feedback         | 1. Tap Application Feedback<br>2. Submit feedback            | Feedback submitted, confirmation received           |
| FS002 | Feature Request              | 1. Tap Feature Request<br>2. Submit request                  | Request submitted, confirmation received            |
| FS003 | Bug Report                   | 1. Tap Bug Report<br>2. Fill details<br>3. Submit            | Bug report submitted, confirmation received         |
| FS004 | Submit Support Ticket        | 1. Tap Submit Support Ticket<br>2. Fill details<br>3. Submit | Ticket submitted, confirmation received             |
| FS005 | Contact Email Link           | Tap contact@ignistech.io email link                          | Default email client opens with address populated   |

#### 4.3.4 Help

| ID    | Description           | Steps                                                              | Expected Result                                    |
|-------|-----------------------|--------------------------------------------------------------------|-----------------------------------------------------|
| HP001 | Access Help Website   | Tap Help link                                                      | Ignis website help section opens in browser         |

#### 4.3.5 General Sidebar Options

| ID    | Description           | Steps                                                              | Expected Result                                    |
|-------|-----------------------|--------------------------------------------------------------------|-----------------------------------------------------|
| SB001 | Logout                | Tap Logout button                                                  | User logged out, returned to login screen           |
| SB002 | Privacy Policy        | Tap Privacy Policy link                                            | Privacy Policy opens in browser or in-app           |
| SB003 | Terms of Use          | Tap Terms of Use link                                              | Terms of Use opens in browser or in-app             |

### 4.4 Nav Bar

#### 4.4.1 Teams

| ID    | Description                 | Steps                                                                             | Expected Result                                    |
|-------|---------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| NB001 | Join Team via Invite Link | 1. Tap Teams in nav bar<br>2. Select "Join via Invite Link"<br>3. Paste or enter invite link<br>4. Confirm | Successfully joined team, team info visible |
| NB002 | Join Team via Code        | 1. Tap Teams in nav bar<br>2. Select "Join via Code"<br>3. Enter team code<br>4. Confirm | Successfully joined team, team info visible |            

#### 4.4.2 Weather

| ID    | Description                        | Steps                                                                             | Expected Result                                    |
|-------|----------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| WE001 | Weather Status Notification       | 1. Open Weather screen<br>2. Observe weather status notification<br>3. Compare with NOAA data | Notification accurately reflects current weather status |
| WE002 | Local Forecast Widget Accuracy    | 1. View Local Forecast Widget<br>2. Compare temperature, conditions with NOAA data | Widget displays accurate local forecast information |
| WE003 | Wind Widget Accuracy              | 1. Check Wind Widget<br>2. Compare wind speed and direction with NOAA data         | Wind information matches NOAA data                  |
| WE004 | Humidity Display Accuracy         | 1. View Humidity information<br>2. Compare with NOAA humidity data                 | Displayed humidity matches NOAA data                |
| WE005 | Precipitation Display Accuracy    | 1. Check Precipitation information<br>2. Compare with NOAA precipitation data      | Precipitation information matches NOAA data         |

##### Forecast Section

| ID    | Description                        | Steps                                                                             | Expected Result                                    |
|-------|----------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| WE006 | Sunrise/Sunset Times Accuracy     | 1. View Sunrise and Sunset times<br>2. Compare with NOAA data                      | Times match NOAA data for the location              |
| WE007 | Relative Humidity Forecast        | 1. Check Relative Humidity forecast<br>2. Compare with NOAA forecast               | Humidity forecast aligns with NOAA predictions      |
| WE008 | SFDI Forecast Accuracy            | 1. View SFDI forecast<br>2. Compare with official SFDI data                        | SFDI forecast matches official data                 |
| WE009 | Precipitation Forecast Accuracy   | 1. Check Precipitation forecast<br>2. Compare with NOAA precipitation forecast     | Forecast matches NOAA precipitation predictions     |
| WE010 | Wind Forecast Accuracy            | 1. View Wind forecast<br>2. Compare with NOAA wind forecast                        | Wind forecast aligns with NOAA predictions          |

##### Hourly Forecast Section

| ID    | Description                        | Steps                                                                             | Expected Result                                    |
|-------|----------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| WE011 | 4-Hour Weather Forecast Accuracy  | 1. View hourly forecasts for next 4 hours<br>2. Compare each hour with NOAA data   | Hourly forecasts match NOAA predictions             |
| WE012 | 4-Hour Precipitation Forecast     | 1. Check precipitation forecasts for next 4 hours<br>2. Compare with NOAA data     | Precipitation forecasts align with NOAA data        |

##### Extended Forecast Section

| ID    | Description                        | Steps                                                                             | Expected Result                                    |
|-------|----------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| WE013 | Toggle Between 4-Day and SFDI     | 1. Switch between 4-day forecast and SFDI forecast<br>2. Verify smooth transition  | Toggle works correctly, displaying appropriate data |
| WE014 | 4-Day Forecast Accuracy           | 1. View 4-day forecast<br>2. Compare each day's forecast with NOAA data            | 4-day forecast matches NOAA extended forecast       |
| WE015 | SFDI Forecast Accuracy            | 1. View SFDI forecast<br>2. Compare with official SFDI extended forecast           | SFDI forecast aligns with official extended data    |

##### General Weather Screen Tests

| ID    | Description                        | Steps                                                                             | Expected Result                                    |
|-------|----------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| WE016 | Refresh Weather Data              | 1. Pull down to refresh or tap refresh button<br>2. Observe update process         | Weather data refreshes, displaying latest information |
| WE017 | Location-based Weather            | 1. Change location<br>2. Verify weather data updates for new location              | Weather data accurately reflects the new location   |
| WE018 | Weather Alerts                    | 1. Simulate or wait for weather alert condition<br>2. Verify alert display         | Weather alerts are prominently displayed when active |

#### 4.4.3 Add Screen

##### General Add Screen Functionality

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| AD001 | Access Add Screen             | Tap Add button in nav bar                                             | Add screen opens with all main categories visible   |
| AD002 | Navigate Categories           | Tap between Fire Ops, Air Ops, and Repair Ops buttons                 | Correct category options display for each button    |

##### Fire Ops

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| AD003 | Add Hot Spot/Spot Fire        | 1. Tap Fire Ops > Fire Ops > Hot Spot/Spot Fire<br>2. Set location<br>3. Save | Point added to map correctly                        |
| AD004 | Add Fire Origin               | 1. Tap Fire Ops > Fire Ops > Fire Origin<br>2. Set location<br>3. Save       | Fire Origin point added to map                      |
| AD005 | Add Safety Zone               | 1. Tap Fire Ops > Safety > Safety Zone<br>2. Set location<br>3. Save         | Safety Zone added to map                            |
| AD006 | Add Hazard Tree               | 1. Tap Fire Ops > Safety > Hazard Tree<br>2. Set location<br>3. Save         | Hazard Tree point added to map                      |
| AD007 | Add Lookout                   | 1. Tap Fire Ops > Safety > Lookout<br>2. Set location<br>3. Save              | Lookout point added to map                          |
| AD008 | Add Hazard                    | 1. Tap Fire Ops > Safety > Hazard<br>2. Set location<br>3. Save               | Hazard point added to map                           |
| AD009 | Add Water Source              | 1. Tap Fire Ops > Water > Water Source<br>2. Set location<br>3. Save         | Water Source point added to map                     |
| AD010 | Add Restricted Water Source   | 1. Tap Fire Ops > Water > Restricted Water Source<br>2. Set location<br>3. Save | Restricted Water Source added to map                |
| AD011 | Add Pump                      | 1. Tap Fire Ops > Accountable Property > Pump<br>2. Set location<br>3. Save   | Pump point added to map                             |
| AD012 | Add Water Tank                | 1. Tap Fire Ops > Accountable Property > Water Tank<br>2. Set location<br>3. Save | Water Tank point added to map                       |
| AD013 | Add Other Property            | 1. Tap Fire Ops > Accountable Property > Other Property<br>2. Set location<br>3. Save | Other Property point added to map                   |
| AD014 | Add Division Break            | 1. Tap Fire Ops > Assignment Breaks > Division Break<br>2. Set location<br>3. Save | Division Break added to map                         |
| AD015 | Add Branch Break              | 1. Tap Fire Ops > Assignment Breaks > Branch Break<br>2. Set location<br>3. Save | Branch Break added to map                           |
| AD016 | Add Zone Break                | 1. Tap Fire Ops > Assignment Breaks > Zone Break<br>2. Set location<br>3. Save | Zone Break added to map                             |
| AD017 | Add Internet Access           | 1. Tap Fire Ops > Communications > Internet Access<br>2. Set location<br>3. Save | Internet Access point added to map                  |
| AD018 | Add Mobile Weather Unit       | 1. Tap Fire Ops > Communications > Mobile Weather Unit<br>2. Set location<br>3. Save | Mobile Weather Unit added to map                    |
| AD019 | Add Repeater                  | 1. Tap Fire Ops > Communications > Repeater<br>2. Set location<br>3. Save    | Repeater point added to map                         |
| AD020 | Add Drop Point                | 1. Tap Fire Ops > Logistics > Drop point<br>2. Set location<br>3. Save       | Drop Point added to map                             |
| AD021 | Add Staging Area              | 1. Tap Fire Ops > Logistics > Staging area<br>2. Set location<br>3. Save     | Staging Area added to map                           |
| AD022 | Add Closure                   | 1. Tap Fire Ops > Logistics > Closure<br>2. Set location<br>3. Save          | Closure point added to map                          |
| AD023 | Add Medical                   | 1. Tap Fire Ops > Logistics > Medical<br>2. Set location<br>3. Save          | Medical point added to map                          |
| AD024 | Add Camp                      | 1. Tap Fire Ops > Logistics > Camp<br>2. Set location<br>3. Save             | Camp point added to map                             |
| AD025 | Add Incident Command Post     | 1. Tap Fire Ops > Logistics > Incident Command Post<br>2. Set location<br>3. Save | Incident Command Post added to map                  |

##### Air Ops

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| AD026 | Add Aerial Hazard             | 1. Tap Air Ops > Air Ops > Aerial Hazard<br>2. Set location<br>3. Save | Aerial Hazard point added to map                    |
| AD027 | Add Airstrip or Airport       | 1. Tap Air Ops > Air Ops > Airstrip or Airport<br>2. Set location<br>3. Save | Airstrip/Airport point added to map                 |
| AD028 | Add Aviation Check Point      | 1. Tap Air Ops > Air Ops > Aviation Check Point<br>2. Set location<br>3. Save | Aviation Check Point added to map                   |
| AD029 | Add Dip Site                  | 1. Tap Air Ops > Air Ops > Dip site<br>2. Set location<br>3. Save      | Dip Site point added to map                         |
| AD030 | Add Mobile Retardant Base     | 1. Tap Air Ops > Air Ops > Mobile Retardant Base<br>2. Set location<br>3. Save | Mobile Retardant Base added to map                  |
| AD031 | Add Helispot                  | 1. Tap Air Ops > Air Ops > Helispot<br>2. Set location<br>3. Save      | Helispot point added to map                         |
| AD032 | Add Helibase                  | 1. Tap Air Ops > Air Ops > Helibase<br>2. Set location<br>3. Save      | Helibase point added to map                         |
| AD033 | Add Sling Site                | 1. Tap Air Ops > Air Ops > Sling Site<br>2. Set location<br>3. Save    | Sling Site point added to map                       |
| AD034 | Add Unimproved Landing Area   | 1. Tap Air Ops > Air Ops > Unimproved Landing Area<br>2. Set location<br>3. Save | Unimproved Landing Area added to map                |

##### Repair Ops

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| AD035 | Add Water Development         | 1. Tap Repair Ops > Repair > Water Development<br>2. Set location<br>3. Save | Water Development point added to map                |
| AD036 | Add Structure Wrap            | 1. Tap Repair Ops > Repair > Structure Wrap<br>2. Set location<br>3. Save | Structure Wrap point added to map                   |
| AD037 | Add Stream Crossing           | 1. Tap Repair Ops > Repair > Stream Crossing<br>2. Set location<br>3. Save | Stream Crossing point added to map                  |
| AD038 | Add Road Repair               | 1. Tap Repair Ops > Repair > Road Repair<br>2. Set location<br>3. Save  | Road Repair point added to map                      |
| AD039 | Add Retardant Avoidance Area  | 1. Tap Repair Ops > Repair > Retardant Avoidance Area<br>2. Set location<br>3. Save | Retardant Avoidance Area added to map               |
| AD040 | Add Resource Location         | 1. Tap Repair Ops > Repair > Resource Location<br>2. Set location<br>3. Save | Resource Location point added to map                |
| AD041 | Add Repair Point              | 1. Tap Repair Ops > Repair > Repair Point<br>2. Set location<br>3. Save | Repair Point added to map                           |
| AD042 | Add Landing or Log Deck       | 1. Tap Repair Ops > Repair > Landing or Log Deck<br>2. Set location<br>3. Save | Landing/Log Deck point added to map                 |
| AD043 | Add Hazard Tree Repair        | 1. Tap Repair Ops > Repair > Hazard Tree Repair<br>2. Set location<br>3. Save | Hazard Tree Repair point added to map               |
| AD044 | Add Fence Cut/Damaged         | 1. Tap Repair Ops > Repair > Fence Cut/Damaged<br>2. Set location<br>3. Save | Fence Cut/Damaged point added to map                |
| AD045 | Add Dozer Push                | 1. Tap Repair Ops > Repair > Dozer push<br>2. Set location<br>3. Save   | Dozer Push point added to map                       |
| AD046 | Add Culvert                   | 1. Tap Repair Ops > Repair > Culvert<br>2. Set location<br>3. Save      | Culvert point added to map                          |
| AD047 | Add Clean Up Area             | 1. Tap Repair Ops > Repair > Clean up Area<br>2. Set location<br>3. Save | Clean Up Area point added to map                    |

#### 4.4.4 Maps Screen

##### General Maps Screen Functionality

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| MP001 | Access Maps Screen            | Tap Maps button in nav bar                                            | Maps screen opens with three tabs visible           |
| MP002 | Navigate Between Tabs         | Tap between PDF Maps, Base Maps, and Layers tabs                      | Correct content displays for each tab               |

##### PDF Maps Tab

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| MP003 | Search PDF Maps               | 1. Enter search term in PDF Maps search bar<br>2. Initiate search     | Relevant PDF maps are displayed in results          |
| MP004 | Upload PDF Map                | 1. Tap add button<br>2. Select PDF file<br>3. Confirm upload          | PDF map successfully uploaded and visible in list   |
| MP005 | View Uploaded PDF Map         | Tap on an uploaded PDF map                                            | PDF map opens and displays correctly on screen      |

##### Base Maps Tab

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| MP006 | Switch to Default Map Layer   | In Base Map layers section, tap Default button                        | Map switches to Default layer                       |
| MP007 | Switch to Hybrid Map Layer    | In Base Map layers section, tap Hybrid button                         | Map switches to Hybrid layer                        |
| MP008 | Switch to Satellite Map Layer | In Base Map layers section, tap Satellite button                      | Map switches to Satellite layer                     |
| MP009 | Upload Offline Base Map       | 1. Tap upload in offline base maps section<br>2. Select area<br>3. Confirm download | Offline base map successfully downloaded and accessible |

##### Layers Tab

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| MP010 | Search Layers                 | 1. Enter search term in Layers search bar<br>2. Initiate search       | Relevant layers are displayed in results            |
| MP011 | Reset Layers                  | Tap Reset Layers button                                               | All layers return to default state                  |
| MP012 | Toggle Layer On/Off           | Tap toggle switch next to a layer                                     | Layer toggles on/off, moves between active/inactive sections |

##### Individual Layer Tests

| ID    | Description                            | Steps                                                    | Expected Result                                    |
|-------|----------------------------------------|----------------------------------------------------------|-----------------------------------------------------|
| MP013 | Toggle Current Fire Perimeters         | Toggle Current Fire Perimeters layer on/off              | Layer displays/hides on map correctly               |
| MP014 | Toggle Current Incidents               | Toggle Current Incidents layer on/off                    | Layer displays/hides on map correctly               |
| MP015 | Toggle AlertCalifornia Cameras         | Toggle AlertCalifornia Cameras layer on/off              | Layer displays/hides on map correctly               |
| MP016 | Toggle California Direct Protection Areas | Toggle California Direct Protection Areas layer on/off | Layer displays/hides on map correctly               |
| MP017 | Toggle Designated Wilderness Area      | Toggle Designated Wilderness Area layer on/off           | Layer displays/hides on map correctly               |
| MP018 | Toggle Dispatch Boundaries             | Toggle Dispatch Boundaries layer on/off                  | Layer displays/hides on map correctly               |
| MP019 | Toggle Fire Weather Warnings/Watches   | Toggle Fire Weather Warnings/Watches layer on/off        | Layer displays/hides on map correctly               |
| MP020 | Toggle Ground Medevac Transport Times  | Toggle Ground Medevac Transport Times layer on/off       | Layer displays/hides on map correctly               |
| MP021 | Toggle Historical Fire Perimeters      | Toggle Historical Fire Perimeters 1991-2023 layer on/off | Layer displays/hides on map correctly               |
| MP022 | Toggle NOAA Weather Radar              | Toggle NOAA Weather Radar layer on/off                   | Layer displays/hides on map correctly               |
| MP023 | Toggle Public Land Ownership           | Toggle Public Land Ownership layer on/off                | Layer displays/hides on map correctly               |
| MP024 | Toggle Recent Heat Detections          | Toggle Recent Heat Detections layer on/off               | Layer displays/hides on map correctly               |
| MP025 | Toggle Repeater Locations              | Toggle Repeater Locations layer on/off                   | Layer displays/hides on map correctly               |
| MP026 | Toggle Severe Fire Danger Index        | Toggle Severe Fire Danger Index layer on/off             | Layer displays/hides on map correctly               |
| MP027 | Toggle Smoke Layer                     | Toggle Smoke layer on/off                                | Layer displays/hides on map correctly               |
| MP028 | Toggle Wind Speed and Direction        | Toggle Wind Speed and Direction layer on/off             | Layer displays/hides on map correctly               |

##### Layer Interaction Tests

| ID    | Description                            | Steps                                                    | Expected Result                                    |
|-------|----------------------------------------|----------------------------------------------------------|-----------------------------------------------------|
| MP029 | Multiple Layer Interaction             | 1. Toggle on multiple layers<br>2. Observe map           | All toggled layers display correctly without conflicts |
| MP030 | Layer Information                      | Tap information icon next to a layer                     | Layer information/legend displays correctly          |
| MP031 | Layer Opacity Adjustment               | Adjust opacity slider for a layer (if available)         | Layer opacity changes accordingly on the map        |

#### 4.5 Search Function

##### General Search Functionality

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| SF001 | Access Search Function        | Tap Search icon or bar                                                | Search interface opens with keyboard active         |
| SF002 | Perform Basic Search          | 1. Enter search term<br>2. Initiate search                            | Results appear, categorized appropriately           |
| SF003 | Clear Search                  | Tap clear (X) button in search bar                                    | Search term cleared, results reset                  |

##### Results Categorization

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| SF004 | Incident Results              | Search for a known incident                                           | Incident appears in "Incidents" category            |
| SF005 | User Map Point Results        | Search for a user-added map point                                     | Point appears in "User Map Points" category         |
| SF006 | Places Results                | Search for a known place                                              | Place appears in "Places" category                  |
| SF007 | Points of Interest Results    | Search for a known point of interest                                  | POI appears in "Points of Interest" category        |
| SF008 | Multiple Category Results     | Perform search that should return results in multiple categories      | Results correctly categorized in respective sections|

##### Distance Display

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| SF009 | Distance to Incident          | 1. Search for incident<br>2. Check distance information               | Accurate distance from user to incident displayed   |
| SF010 | Distance to User Map Point    | 1. Search for user map point<br>2. Check distance information         | Accurate distance from user to map point displayed  |
| SF011 | Distance to Place             | 1. Search for place<br>2. Check distance information                  | Accurate distance from user to place displayed      |
| SF012 | Distance to Point of Interest | 1. Search for point of interest<br>2. Check distance information      | Accurate distance from user to POI displayed        |
| SF013 | Update Distance on Movement   | 1. Perform search<br>2. Change user location<br>3. Check distances    | Distances update accurately based on new location   |

##### Search Functionality Tests

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| SF014 | Partial Text Search           | Enter partial name of known point                                     | Relevant results appear in appropriate categories   |
| SF015 | Misspelled Search             | Enter slightly misspelled name of known point                         | Correct point appears in results if within tolerance|
| SF016 | Search with Special Characters| Enter search term with special characters (e.g., hyphens, apostrophes)| Correct results appear, handling special characters |
| SF017 | Search Result Limit           | Perform broad search likely to return many results                    | Results limited to manageable number, option to view more |
| SF018 | No Results Handling           | Enter search term unlikely to have any results                        | Appropriate "No results found" message displayed    |

##### Interaction with Search Results

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| SF019 | Select Incident Result        | 1. Search for incident<br>2. Tap on incident in results               | Map centers on incident, displays incident details  |
| SF020 | Select User Map Point Result  | 1. Search for user map point<br>2. Tap on point in results            | Map centers on point, displays point details        |
| SF021 | Select Place Result           | 1. Search for place<br>2. Tap on place in results                     | Map centers on place, displays place details        |
| SF022 | Select Point of Interest      | 1. Search for POI<br>2. Tap on POI in results                         | Map centers on POI, displays POI details            |

##### Performance and Edge Cases

| ID    | Description                   | Steps                                                                 | Expected Result                                    |
|-------|-------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| SF023 | Search Performance            | Perform multiple searches in quick succession                         | App remains responsive, results load quickly        |
| SF024 | Large Result Set Handling     | Search for a term likely to return a large number of results          | Results load efficiently, option to load more       |
| SF025 | Offline Search Functionality  | 1. Enable airplane mode<br>2. Perform search                          | Search works for offline content, message for online-only results |
| SF026 | Recent Searches               | 1. Perform several searches<br>2. Check recent searches (if feature exists) | Recent searches displayed accurately                |

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

| Risk | Mitigation |
|------|------------|
| Device availability | Maintain a diverse device inventory |
| iOS version compatibility | Test on multiple iOS versions |
| Network conditions | Use Charles Proxy for network simulation |

