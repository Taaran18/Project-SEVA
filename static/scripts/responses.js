function getBotResponse(input) {
  console.log(input);
  if (
    input == "what are the requirements for applying for a job" ||
    input == "Do I need to submit any document for applying for a job " ||
    input == "requirement for a job application"
  ) {
    return "you have to fill in the details in the form which automatically creates a resume and then answer the questions by the organization then you can apply for the job posting.";
  } else if (
    input == "from where can I make a resume" ||
    input == "is there any support available to help with a resume" ||
    input == "help resume"
  ) {
    return "Our portal has features that help in building a resume for you according to the details that you fill in the form. You can navigate to that option by going to the resume tool option in the n navigation bar.";
  } else if (
    input == "how will I know if I get selected for a job" ||
    input == "application status"
  ) {
    return "As you will receive e notification on the portal if you get selected for a job.";
  } else if (
    input ==
      "how can I see the progress of the application for the job that I posted" ||
    input == "job posting progress"
  ) {
    return "you can view the progress by going on the dashboard which shows details like the number of opportunities you posted and, progress made by applicants i.e. resumes uploaded, etc. based on which you can then shortlist candidates.";
  } else if (
    input == "how much time it takes to register a new user" ||
    input == "new user registration time"
  ) {
    return "Registration is very quick, as soon as a new user or organization fills in the detail it registers the user.";
  } else if (input == "what is your objective" || input == "your objective") {
    return "Project SEVA aims to provide a platform for retired and discharged officers to avail of job opportunities that make it easy for them to explore and grab opportunities. At the same time, it helps organizations get experienced employees for the organizations.";
  } else if (input == "when were you made") {
    return "I was made as a result of a project a 48 hours Poornima hackathon 2023, where Akshay Kumar goyal, Taaran Jain, Abhijeth Pillai, and Navdeep Doriya made me their project for the hackathon";
  } else if (input == "can I edit my resume more than once") {
    return "Yes, you can edit your resume as many times as you want; each time you change those details, it will get automatically updated.";
  } else if (
    input == "from where can I get details to contact the admin" ||
    input == "contact the admin"
  ) {
    return "the contact information can be accessed from the contact us tab.";
  } else if (input == "I love your program.") {
    return "It is all because of the hardwork of my makers";
  } else {
    return "Try asking something else!";
  }
}
