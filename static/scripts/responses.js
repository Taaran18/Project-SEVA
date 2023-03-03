function getBotResponse(input) {
    console.log(input);
    if (input == "what are the requirements for applying for a job" || input == "Do I need to submit any document for applying for a job " || input == "requirement for a job application") {
        return "you have to fill in the details in the form which automatically creates a resume and then answer the questions by the organization then you can apply for the job posting.";
    } 
    else if (input == "from where can I make a resume" || input == "is there any support available to help with a resume" || input == "help resume") {
        return "Our portal has features that help in building a resume for you according to the details that you fill in the form. You can navigate to that option by going to the resume tool option in the n navigation bar.";
    }  
    else if (input == "how will I know if I get selected for a job" || input == "application status") {
        return "As you will receive e notification on the portal if you get selected for a job.";
    } 
    else if (input == "how can I see the progress of the application for the job that I posted" || input == "job posting progress"){
        return "you can view the progress by going on the dashboard which shows details like the number of opportunities you posted and, progress made by applicants i.e. resumes uploaded, etc. based on which you can then shortlist candidates.";
    }
    else {
        return "Try asking something else!";
    }

}