class Resume:
    """
    QA profile summary and all
    """
    def __init__(self):
        self.name = "Sabbir-Ul-Alam"
        self.email = "sabbir.ul.alam.sabbir@gmail.com"
        self.professional_experience = self.Experience
        self.professional_projects = self.ProfessionalProjects
        self.education = self.Education
        self.skills = self.Skills
        self.pet_projects = self.PetProjects
        self.social_links = self.Links

    class Experience:
        def cheq_cantaloupe_platform(self):
            info = { "role": "Senior SQA", "duration": "Jun 2024 - May 2025", "location": "Remote, US" }
            tasks = [
                "Participated in spec review meetings and collaborated with product teams to analyze requirements",
                    "Defined testing scope by reviewing requirements, specifications, designs, and developed end-to-end au-"
                    "tomation scripts using Cypress"]
        def tigerit_bangladesh_ltd(self):
            info = { "role": "Senior SQA", "duration": "July 2022 - May 2024", "location": "Bangladesh" }
            tasks = [
                "Led a team of four QA engineers, managing task assignments and ensuring project success",
                "Created comprehensive release and test plans to align with sprint timelines and ensure timely delivery",
                "Took ownership of critical modules, overseeing their development, testing, and successful deployment to"
                "production",
                "Designed and optimized a CI/CD pipeline for efficient testing and deployment",
                "Participated in commit reviews to ensure code quality and adherence to standards. Conducted root cause"
                "analysis of bugs and production issues to drive long-term solutions and improve system stability" ]
        def tigerit_bangladesh_ltd(self):
            info = { "role": "SQA", "duration": "July 2019 - June 2022", "location": "Bangladesh" }
            tasks = [
                "Conducted functional, performance, regression, and user acceptance testing",
                "Developed Python scripts for automating test data generation and log filtering",
                "Collaborated with developers to investigate bugs and optimize workflows" ]