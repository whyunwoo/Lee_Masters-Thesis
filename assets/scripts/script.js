const consentHTML = `
    <div style="font-size: 80%; max-width:700px">
        <h2>Informed Consent</h2><br>
    
        <div style="text-align: left">
        <h3>Streetscape Perceptions</h3>
        <b>HUM00189138</b>
        <br><hr>
    
        <h4>DESCRIPTION</h4>
        <p>
            In this study, you will view Google Street View images. You will then answer questions about your impressions of the streetscapes presented in those images.

        </p><br>
    
        <h4>TIME INVOLVEMENT</h4>
        <p>Your participation will take approximately 30 minutes.</p><br>
    
        <h4>RISKS AND BENEFITS</h4>
        <p>
           The risks associated with this study are minimal. The benefits which may reasonably be expected to result from this study are none.  We cannot and do not guarantee or promise that you will receive any benefits from this study.  
        </p><br>

        <h4>PAYMENTS</h4>
        <p>You will receive .5 credit  for your participation.</p><br>

        <h4>SUBJECT'S RIGHTS</h4>
        <p>
            If you have read this form and have decided to participate in this project, please understand your participation is voluntary and you have the right to withdraw your consent or discontinue participation at any time without penalty or loss of benefits to which you are otherwise entitled.  The alternative is not to participate.  You have the right to refuse to answer particular questions.  
 
        </p>
    
        <p>
            Your individual privacy will be maintained in all published and written data resulting from the study. Your responses will be kept confidential: you are given a participant code, and no one, not even the research team, can match that code with your identity. Your collected information may also be shared with other researchers as part of our dataset.
        </p><br>
    
        <h4>CONTACT INFORMATION</h4>
        <p>
           Questions:  If you have any questions, concerns or complaints about this research, its procedures, risks and benefits, contact the Protocol Director, Nicholas Camp, npcamp@umich.edu, (443) 851-6783.
        </p>
    
        <p>
            If you have questions about your rights as a research participant, or wish to obtain information, ask questions or discuss any concerns about this study with someone other than the researcher(s), please contact the following:
            <br><br>
    
            University of Michigan<br>
            Health Sciences and Behavioral Sciences Institutional Review Board
            (IRB-HSBS)<br>
            2800 Plymouth Road <br>
            Building 520, Room 1169 <br>
            Ann Arbor, MI 48109-2800 <br>
            Telephone: 734-936-0933 or toll free (866) 936-0933 <br>
            Fax: 734-936-1852 <br />
            E-mail: irbhsbs@umich.edu <br>
        </p>
    
        <p>
            You can also contact the University of Michigan Compliance Hotline at 1-866-990-0111. You may also print this consent form to keep.
        </p>
        <br>
    
        <div class="alert alert-warning"><b>
            Do you consent to participate in this study? If you consent to participate in this study, please click “yes”. If you select "no", you will be directed out of the survey.

        </b></div>
        </div>
    </div>
`


/* WELCOME MESSAGE */
const html_intro1 = `
<div class="text-container">
    <h1>Welcome to the study!</h1>
    
    <div class="text-left">
        <p>
            In this study, we are interested in how people think about different Google Street View images. Google Street View takes pictures of streets used for Google Earth and Google Maps. You’ll see Google Street View images of different places and answer some questions about each one.
        </p>
    </div>
    <img src = "assets/img/example.png" width = 500px, height = auto>
    <br>
<br>
`;


const html_intro2 = `
        <style>
            img.small {
            max-width: 100px;
            }
            li {
            text-indent: 40px;
            }
        </style>

        <div class="text-container text-left">
            <p>For each picture, we’d like your impressions of the scene:</p>
            
            <hr>
                Are there <b>clear, distinct boundaries</b> between objects in the scene, or are the <b>boundaries ambiguous or unclear</b>?
                
                <li>clear, distinct boundaries: <img class="small" src="assets/img/ambiguous-low.png"></li>
                <li>ambiguous or unclear boundaries: <img class="small" src="assets/img/ambiguous-high.png"></li>
            <hr>
            <br>
                Are there <b>only a few different objects</b> in the scene, or is there <b>a large number</b>?
            <br><br>
            <hr>
                Are only <b>a few parts</b> of the scene <b>invisible or obscured</b>, or are <b>many parts invisible or obscured</b>?
                
                <li>a few parts invisible or obscured: <img class="small" src="assets/img/invisible-low.png"></li>
                <li>many parts invisible or obscured: <img class="small" src="assets/img/invisible-high.png"></li>
            <hr>
            <br>
                Does the scene look <b>organized</b> or <b>chaotic</b> to you?
            <br><br>
            <hr>
            
            <p>
                There are no right or wrong answers: we are interested in <b>your</b> impression. Note that some images might have individual buildings or faces blurred for privacy. Please ignore these when making your judgments.
            </p>
        </div>
        <br>
    `;


const html_intro3 = `
    <div class="text-container text-left">
        <p>Please make sure you are doing this study in an area where you can focus and complete the survey in one sitting.</p>

        <p>Don’t spend too much time on any one picture- go with your gut impression!</p>
        
        <p>The study should take about 20 minutes. We’ll let you know when you’re halfway through.</p>
    </div>
        
    <h3>Ready? Click next to get started!</h3>
    <br>
`;


var half_way_prompt = `
<h3>You are now half way through the study.</h3>
<p>Please take a quick, 15-second break before you continue.</p>
<img src='assets/img/countdown-15.gif'>
<p>The study will automatically advance forward after the countdown is complete. However, you may click "Next" to advance forward now if you wish.</p>
`;

const preambleDemog = `
        <br>
        <p>Thank you for your responses. Finally, we’d like to ask you a few questions about yourself.</p>
        <hr>
        <br>
    `;


const debriefHTML = `
    <h3>Thank you for participating in the study!</h3>
    
    <div style="text-align: left; max-width: 700px; font-size: 80%">
        <p>
            In this study, we were interested in how environments in different places influence perception. Specifically, we want to know how complex the environment appears in different cities around the world. You rated images from different cities in the United States and Japan; your answers will help us understand these differences in the physical environment. 
        </p>

        <p>
          Interested in learning more? Check out these articles: <br>
                - Miyamoto, Y., Nisbett, R. E., & Masuda, T. (2006). Culture and the physical environment: Holistic versus analytic perceptual affordances. Psychological science, 17(2), 113-119.<br>
                - Masuda, T., Ishii, K., & Kimura, J. (2016). When does the culturally dominant mode of attention appear or disappear? Comparing patterns of eye movement during the visual flicker task between European Canadians and Japanese. Journal of Cross-Cultural Psychology, 47(7), 997-1014.<br>
        </p>
    
        <p>
            If you have further questions about the study or your participation, please contact the protocol director at npcamp@umich.edu. 
        </p>
    </div>
`;


var endStudyNoConsent_prompt = `
    <h3>You have declined the informed consent form.</h3>
    <p>Please exit this window and return this study on SONA.</p>
    `;

var endRedirectPrompt = [`You've reached the end of the survey. <br><br> 
<b>Do not close or refresh this window.</b><br>
In the next page, you will see a pop-up like below after a few moment.<br><br>
<img src='assets/img/chrome.PNG'> <br><br>
Press the <b>'Leave'</b> button to exit from the experiment without losing your record.<br>
You will be automatically redirected to SONA once you click the <b>'Leave'</b> button. <br><br>`
]
