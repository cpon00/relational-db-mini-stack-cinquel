

## Cinquel

##### https://github.com/lmu-cmsi3520-fall2021/relational-db-mini-stack-cinquel

| Category | Feedback | Points |
| --- | --- | ---: |
| _netflix-practice.md_ | Queries that perform the requested operations correctly: 1, 2, 3, 4, 5, 6, 7<br><br>However, the writeup for Query 6 is a tad out of sync: the natural language states an average ≥ 4, the screenshot asks for an average > 4, and the query text is for an average > 3. Um which is it 😅 (–1)<br><br>Some nice continuity across queries 🐕🦮🐩🐕‍🦺 | 27/28 |
| _about.md_ | | |
| • Link to dataset | Link to dataset was provided | 1/1 |
| • Description of dataset | Dataset is described well alongside possible applications that would use it; sample queries make sense for the domain. Overall good detail and clear organization | 4/4 |
| _.gitignore_ | _.gitignore_ contains appropriate ignores |  |
| _schema.pdf_ | Schema diagram effectively communicates the intended design of the database, with proper notation of referring keys. Primary keys are less clearly indicated; although they can be inferred, it would have been safest to follow the notation that was given (–1)<br><br>Although the referring-key notation is correct, some arrows are in the wrong direction. Remember anything that _references_ something has the arrow pointing toward what is being references. This isn’t always correctly done in the diagram (–1)<br><br>Not a super huge deal, but the naming convention for tables representing many-to-many relationships typically separates the referenced tables with an underscore (e.g., _movie_genre_, _movie_keyword_) | 3/5 |
| _schema.sql_ | Schema SQL appears to follow the design and executes without errors | 5/5 |
| Loader programs | Data loaders run without problems—but why were the credit records truncated? “There are only a few relevant/main characters/actors for our purposes” doesn’t ring true for me. I took out the limitation and everything loaded fine<br><br>A side question is why you chose the `INSERT` route rather than `COPY` for the credits—as stated in the case study, `COPY` is _much_ faster! No deduction here because the only impact is speed and your dataset isn’t that large, but if things scaled up further, that savings would definitely be felt | 10/10 |
| _queries.md_ | Queries 1–7 are functional and look appropriate for the domain<br><br>Query 2 might have been a little more interesting if you had chosen a character who has been played by _different performers_ (e.g., Batman, James Bond, Queen Elizabeth, Athena, etc.) | 20/20 |
| DAL module | | |
| • Configuration/setup | Configuration code uses library correctly and properly separates configuration information as an environment variable | 7/7 |
| • Retrieval | Wow, more than one retrieval function! They all look appropriate for the domain and appear to work as intended | 4/7 |
| • CUD | `insert_movie` and `delete_movie` successfully make their respective changes to the database. However, `delete_movie` doesn’t return any indication of how things went. It would have been good to look up the API for this to see if some kind of return value can be produced (e.g., to indicate how many records were deleted) (–2) | 8/7 |
| • Mix of styles | The DAL uses all available implementation styles | 3 |
| DAL programs | • _search_movies_by_title.py_ checks the argument count and provides help when needed, but its results display can be more end-user friendly. Looks like you’re just printing raw tuples—not a good choice for end-user programs. I mean, exposing `datetime.date`? You should know better (–0.75). It also does _not_ display any readable message when there are no matches (–0.75)<br><br>(of note: even if _get_popularity_of_movie.py_ worked better—it does not—it wouldn’t be appropriate to skip the deductions because these are genuine points of improvement that need to be called out)<br><br>• _insert_movie.py_ checks the argument count but is quite fragile—stack traces are exposed (for example, with a bad data type like supplying a string for `popularity`). You aren’t expected to handle those situations, but you could have kept the stack trace from blurting out (–0.75)<br><br>* _remove_movie.py_ has the same issues (–0.75) and also doesn’t state whether a deletion actually happened. However that is more of a limitation of the underlying DAL function so we’ll let that slide for the program | 3/6 |
| Code maintainability | No major code maintainability issues were found |  |
| Code readability | No major code readability issues were found |  |
| Version control | Good commit frequency and count, with sufficiently informative messages; distribution of commit count is a little lopsided but I didn’t hear about any internal issues so I’ll presume that the division of labor is acceptable to all involved |  |
| Punctuality | First commit on 10/6 2:08pm; last commit on 10/18 12:26am |  |
| | **Total** | **95/100** |
