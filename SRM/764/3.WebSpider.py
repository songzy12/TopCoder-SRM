# ## Problem Statement
# You are writing software that will spider a web site (that is, it visits all links on the homepage, then visits all links on those pages, etc.), and travels three levels deep. You have a list of all the links found in the first pass, in the second pass, and in the third pass.
# You are given a tuple (string), firstPass, containing a list of all the links visited from the home page. They will all be in the form "page", "subfolder/page", "subfolder/subfolder/page", etc. There may be any level of depth to the subfolders.
# You are given a tuple (string), secondPass, containing a list of all the links found in the second pass (by visiting the links found on the home page). Each element is of the form "pageNumber address", where pageNumber is the index (from 0) of the page from firstPass on which the link was found. address is formatted similarly to the elements of firstPass, with the added possibility of a subfolder named "..", which means "go to the parent folder". However, ".." can only appear as the first subfolder, or if all the previous subfolders are also "..". So, if the homepage contains a link to "reports/sales.htm", sales.htm is in the reports folder. If that page then contains a link to "products.htm", then products.htm is also in the reports folder. However, if that page contains a link to "../home.htm", then that is a link back to a page in the root folder.
# You are finally given a tuple (string), thirdPass, indicating all of the links found in the third pass. It is formatted exactly as in secondPass, but the page numbers here refer to the index of the page from secondPass. In all cases, the links reference will be relative paths. In particular, they will never begin with a '/' character.
# You are to return an integer indicating the number of distinct pages (not including the initial homepage) visited during this crawl of the web site.
#
# ## Constraints
# - firstPass will contain between 1 and 50 elements, inclusive.
# - secondPass and thirdPass will contain between 0 and 50 elements, inclusive.
# - Each string in the input will be a maximum of 50 characters.
# - A link will be formatted as a sequence of letters, numbers, periods and slashes.
# - No link will contain leading, trailing or double slashes, and the file name will contain at least one letter or number.
# - Each element of firstPass will be formatted as a single link.
# - Each element of secondPass and thirdPass will be formatted as an integer with no extra leading zeros, followed by a space and a link.
# - The integers in secondPass and thirdPass will reference valid pages in firstPass and secondPass, respectively.
# - None of the links will go above the root directory.
# - A subfolder containing only periods will only be ".." and is only allowed in secondPass or thirdPass. Furthermore, it must be either the first subfolder or else all the preceding subfolders must also be "..". Hence, links like "reports/../home.htm" and ".../abc.htm" are not allowed.
class WebSpider:
    def countPages(self, firstPass, secondPass, thirdPass):                
        pass