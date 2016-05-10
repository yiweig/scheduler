# class-scheduler

## Summary
(Might need to clarify some of this) General idea: class scheduler that plans out your class over 4 years based on previous course information obtained through scraping/manual input. Since courses typically follow a somewhat predictable pattern, we can plan out future class schedules with a fair amount of certainty. Of course, faculty/curriculum changes, and other external events will cause drastic changes, but this is an inherent risk anyways. The benefit we provide is that we can automatically adjust the schedule once there is a change, with no other input from users other than indicating that a change is needed due to an unregistered class.


## Notes
- Two main path options available to users: speed vs prestige (maybe another name?)
 - *Speed*: fastest way to graduation
 - *Prestige*: class schedule which includes classes taught by the most prestigious professors (see below on details of how to determine prestige) 

- **Prestige**:
A metric similar to the [h-index](https://en.wikipedia.org/wiki/H-index "h-index"), but we will try to improve objectivity and relevance to students by including new features in addition to those considered by the h-index. These can include, but are not limited to, number of publications, number of citations, the professor's undergraduate + graduate schools, some normalized score of papers/citations over the course of their career, composition of current PhD candidates, previous employment, whether they have a research lab, grant money, grant types, grant sources. These features are tentative, and are listed here roughly in order of descending importance.

We will start with Emory first, since that is where we are most familar. We'll see where it goes (if anywhere).

Some features:

- User profiles, so users can save/load schedules, as well as compare themselves to students in other schools of the same field of study. We would probably need to create some kind of metric to score students as well (but we'll cross this bridge when we get there) 

## Tech (for the 1st iteration)
Django  
PostgreSQL (and possibly MongoDB)

