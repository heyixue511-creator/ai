# Domain visualization using VxInsight® for science and technology management ( etc.) (z-library.sk, 1lib.sk, z-lib.sk)

Domain Visualization Using VxInsight(cid:1) for Science and
Technology Management

Kevin W. Boyack, Brian N. Wylie, and George S. Davidson
Sandia National Laboratories*, P.O. Box 5800, MS-0318, Albuquerque, NM 87185.
E-mail: kboyack@sandia.gov

We present the application of our knowledge visualiza-
tion tool, VxInsight(cid:1), to enable domain analysis for sci-
ence and technology management within the enterprise.
Data mining from sources of bibliographic information is
used to deﬁne subsets of information relevant to a tech-
nology domain. Relationships between the individual ob-
jects (e.g., articles) are identiﬁed using citations, de-
scriptive terms, or textual similarities. Objects are then
clustered using a force-directed placement algorithm to
produce a terrain view of the many thousands of objects.
A variety of features that allow exploration and manipu-
lation of the landscapes and that give detail on demand,
enable quick and powerful analysis of the resulting land-
scapes. Examples of domain analyses used in S&T man-
agement at Sandia are given.

Introduction

Management of science and technology (S&T) has long
been a labor-intensive process, relying extensively on the
accumulated knowledge of those within the enterprise. Ac-
tivities such as technology planning, roadmapping, and the
identiﬁcation of promising or potentially disruptive technol-
ogies have been time consuming, and have relied on incom-
plete information and expert opinion. In addition, the risks
associated with poorly managing technology investments
have never been greater.

Fortunately, with the increasing availability of informa-
tion sources, computing power, advanced visualization
techniques, and the emergence of practices such as domain
analysis (Hjorland & Albrechtsen 1995), S&T management

Received July 6, 2001; revised December 14, 2001; accepted Decem-

ber 14, 2001

*Sandia is a multiprogram laboratory operated by Sandia Corporation, a
Lockhead Martin Company, for the United States Department of Energy. The
authors gratefully acknowledge the support of Chuck Meyers and the Labo-
ratory Directed Research and Development Program, Sandia National Labo-
ratories, U.S. Department of Energy, under contract DE-AC04-94AL85000.

© 2002 Wiley Periodicals, Inc. ● Published online 3 May 2002 in Wiley
InterScience (www.interscience.wiley.com). DOI: 10.1002/asi.10066

can be done much more rapidly and with increasing robust-
ness than in the past. Effective practices must become an
integral part of the S&T sponsor’s business operations, but
at the same time the knowledge of subject matter experts
must continue to play a crucial role (Losiewicz, Oard, &
Kostoff, 2000).

The ﬁelds of bibliometrics and citation analysis have
been used to inform S&T management over the years. Much
of the work in these ﬁelds has been aimed at developing and
evaluating techniques, using domains well known to the
authors, for example, the domain of information science in
White and McCain (1998). Although these studies have
elaborated on knowledge communities, structure of do-
mains, and trends within those domains, few studies have
sought to answer detailed questions of a competitive na-
ture— questions such as “Who are my competitors in this
domain?” “What is their technology?” “Will their technol-
ogy disrupt my business?” “Should I partner? . . . and if so,
with whom?” This is perhaps not surprising in that the
results of such studies would contain proprietary informa-
tion that a sponsor would not want to make public.

Detailed questions such as these about one’s competition
are critical to robust S&T management. Yet, they seem to
have been largely ignored by practitioners of information
science, and left to market researchers who too often make
little use of the scientiﬁc literature and its wealth of com-
petitive information.

At Sandia National Laboratories, we are making use of
domain visualization as input
to the S&T management
process for many of our technologies. Although some of this
work has been done from an academic viewpoint, the ma-
jority of our studies are done to provide concrete answers to
speciﬁc questions in a narrow technology domain, and thus
guide our S&T investment, development, and partnering
strategies in those domains.

We perform these detailed domain analyses using our
knowledge visualization tool, VxInsight(cid:2) (Beck, Boyack,
Bray, & Siemens, 1999; Davidson, Hendrickson, Johnson,
Meyers, & Wylie, 1998), which transforms information
such as documents, patents, or even genomic data into an

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY, 53(9):764 –774, 2002

intuitive visual format that is easy to interpret and that
allows natural navigation and query. VxInsight presents
information as a landscape, a familiar representation that we
are adept at interpreting, and that allows very large data sets
to be represented. The landscape representation conveys
signiﬁcant information about the implicit structure of the
data, providing context for the analyst’s exploration and
queries of the database.

In this article we provide a review of related work and
tools, a description of the VxInsight tool and its function-
ality, and then report on features of speciﬁc domain analyses
used for competitive intelligence purposes at Sandia. The
article concludes with a summary of lessons learned and
thoughts on the future of S&T management.

Related Work

Science Mapping Studies

Various efforts to map the structure of science have been
undertaken over the years. Science mapping studies are
typically focused at either the macro- or microlevel. At a
macrolevel such studies seek to determine the basic struc-
tural units of science and their interrelationships (Bassecou-
lard & Zitt, 1999; Nederhof & van Wijk, 1997). Some
macrolevel studies also allow exploration of the ﬁne-scale
structure underlying the global networks (Small, 1999).
However, the majority of science mapping studies are per-
formed at
the discipline or domain level (Leydesdorff,
1994; Noyons & van Raan, 1998; McCain, 1998; Spasser,
1997; White & McCain, 1998), and seek to inform science
policy and technical decision makers. Studies at both levels
probe the dynamic nature of science and the implications of
the changes. Alternate approaches with more applied goals
(such as S&T management) include textual data mining
(Losiewicz, Oard, & Kostoff, 2000) and database tomogra-
phy methods (Kostoff, Eberhart, & Toothman 1999), and
are usually applied at the discipline level.

A variety of databases and methods have been used for
these studies. Primary among databases are the Science
Citation Indexes (SCI and Social SCI) from the Institute for
Scientiﬁc Information (ISI), which have gained widespread
acceptance for bibliometric studies. Science and technology
maps are most often based on computed similarities be-
tween journal articles using citation analysis (Small, 1999),
or cooccurrence or coclassiﬁcation using keywords, topics,
or classiﬁcation schemes (Nederhof & van Wijk, 1997;
Noyons & van Raan, 1998; Spasser, 1997). Studies to
identify intellectual or social networks are performed using
author cocitation analysis (Chen, Paul & O’Keefe, 2001;
White & McCain, 1998) or on the basis of coauthorship
(Newman, 2001). Macrolevel maps can be based on journal
intercitation patterns (Bassecoulard & Zitt, 1999; Leydes-
dorff, 1994; McCain, 1998). Citation and classiﬁcation
based techniques have been used recently to map technol-
ogy domains based on U.S. patents (Boyack, Wylie, David-
son, & Johnson, 2000). Latent semantic analysis (Landauer,

Foltz, & Laham, 1998; Borner, 2000), a memory-intensive
text-based process, has also become more prominent as
computing resources have increased.

Once relationships between objects (articles, terms, au-
thors, etc.) have been deﬁned and a similarity matrix (based
on cocitation or cooccurrence, etc.) has been computed,
algorithms are used to cluster the data. Common clustering
methods for producing maps include hierarchical clustering,
k-means algorithms, multidimensional scaling, principal
components analysis, and self-organizing maps. Histori-
cally, the standard mapping output has been a circle plot
where each cluster is represented by a circle sized to rep-
resent the number of documents. Links between circles
provide relationship information including the strength of
the link. Traditionally, map outputs have been paper-based,
and only resolve structure at a few discrete levels. However,
in recent years, several systems have been reported that use
a computer display and allow some navigation of the map
space.

Visualization Techniques

SENTINEL (Fox, Frieder, Knepper, & Snowberg, 1999)
is a Harris Corporation package that combines a retrieval
engine using n-grams and context vectors for effective
query with a visualization system called VisualEyes™. The
visualization tool allows the user to interact with document
clusters in a three-dimensional space. Chen (1999) uses a
VRML 2.0 viewer in conjunction with Generalized Simi-
larity Analysis to display authors (as spheres) and the cor-
responding Pathﬁnder linkage network that has been calcu-
lated from an author cocitation analysis. Chen, Paul, and
O’Keefe (2001) expand this work to provide citation rates
as multicolored bars rising out of each sphere in their maps.
The CAVE environment at Indiana University is used by
Bo¨rner (2000) to interface with documents in a virtual
library. Documents are clustered using latent semantic anal-
ysis. Varying shapes, colors, and labels are used to identify
features of each document. Document details are available
on demand through a hypertext link.

Self-organizing maps have been used in many venues,
including the organization of document spaces (Honkela,
Kaski, Kehoven, & Lagus, 1998). These maps are used to
position documents, and then display them in a two-dimen-
sional contour map-like display in which color represents
density. Peak labels can be generated automatically, and
some limited navigational and retrieval capabilities are of-
ten provided.

Two packages that are more similar to Sandia’s VxIn-
sight are SCI-Map developed by ISI (Small, 1999), and the
SPIRE suite of tools that originated at Paciﬁc Northwest
National Laboratory (Hetzler, Whitney, Matucci, &
Thomas, 1998; Wise, 1999). SCI-Map uses a hierarchically
nested set of maps to display the document space at varying
levels of detail. This nesting of maps allows movement
between levels. Each map is similar to the traditional circle
plot, where the size of the circle can indicate the density of

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

765

FIG. 1. The process of moving similar items close together and simul-
taneously pushing dissimilar objects away.

documents contained in the circle, or some measure of
importance. Relationships at each discrete level are indi-
cated by links between circles.

Like VxInsight, SPIRE maps objects to a two-dimen-
sional plane so that related objects are near each other, and
provides tools to interact with the data. SPIRE has two
visualization approaches. In the Galaxies view, documents
are displayed as a scatter plot. This interface allows drilling
down to smaller sections of the scatter plot, and provides
some summarization tools. In the Themescape view, a high-
level terrain display, similar to that in VxInsight, is used.
Themescape visualizes speciﬁc themes as mountains and
valleys, where the height of a mountain represents the
strength of the theme in the document set.

VxInsight Tool

The Sandia VxInsight tool consists of two parts—a force-
directed placement ordination routine (named VxOrd), and the
visualization engine.

Ordination Routine (VxOrd)

VxOrd is used in conjunction with the VxInsight appli-
cation to calculate the layout of data objects on a 2D plane
using the similarities between the data objects (Davidson,
Wylie, & Boyack 2001). At the most basic level the VxOrd
algorithm tries to place similar objects close together and
dissimilar objects far apart. The example shown in Figure 1
demonstrates this basic principle. In VxOrd, the process is
achieved by moving the objects randomly around the solu-
tion space via a technique similar to “simulated annealing.”
The criteria for moving a node is the minimization of energy
given by:

Ex,y (cid:1)(cid:1) (cid:2)

n

i(cid:1)0

2(cid:3)(cid:3) (cid:3) Dx,y

(cid:2)wi (cid:2) li

where Ex,y is the energy of a node with n edges at a speciﬁc
x, y location, wi is the similarity between that node and the
node connected by edge i, li is the Euclidean distance
between that node and the node connected by edge i, and
Dx,y is a density measure with respect to the area around
point x,y.

The function Dx,y can be computed in many different
ways. A brute force approach is to base Dx,y on the distance

to all other nodes. Because each node would have to calcu-
late its distance from each other node, this approach would
take N comparisons (where N (cid:1) number of nodes in the
graph) for each determination of Dx,y. All nodes must com-
pute Dx,y when determining their energy at a speciﬁc loca-
tion x,y; thus, the algorithm would require O(N2) running
time, which for large datasets is computationally expensive.
We compute Dx,y as a density ﬁeld to which each node
contributes. The density ﬁeld is constructed as the sum of
the energy footprints from each node, where the energy
footprint is a function of 1/r2 from the node location. Having
each node contribute an energy footprint to the density ﬁeld
requires O(N) time. Having each node look up the value of
the density ﬁeld at its current location requires O(N) time.
Thus, the overall computational requirement for the density
ﬁeld implementation is still O(N).

VxOrd accepts a list of precomputed similarities and
outputs an x,y location for each object. Alternately, it ac-
cepts a list of directional edges such as literature citation
references and computes similarities based on direct and
cocitation linkages (see Small, 1997) prior to calculating an
x,y location for each object.

User Environment

VxInsight accepts the x,y coordinates generated by VxOrd
(or by another clustering routine), and overlays the 2D plane
with a 3D virtual landscape that looks like a mountain range.
This 3D environment is readily understood because there is
only a small cognitive step between seeing the virtual terrain
and then exercising our innate human expertise in navigating
through real terrains.

Given that the ordination algorithm has placed similar
objects (e.g., documents) close together, very similar items
cluster together and form mountains on the terrain. Related
clusters of information occur in mountains that are close to
each other. The landscape is displayed “on the ﬂy” with the
height of each mountain being proportional to the number of
objects beneath it. To explain the nature of the landscape,
VxInsight dynamically generates labels for the most signif-
icant mountains from metadata associated with the objects,
revealing the content of the objects that comprise the moun-
tain. For instance, if article titles are selected as the basis for
labeling, VxInsight will display the two most common
words found in the titles comprising a mountain as the label
for that mountain. The tool supports multiresolution zoom-
ing into the terrain to explore interesting regions in greater
detail, which reveals structure on multiple scales. Following
each mouse click the landscape is recalculated to give a
new, higher resolution view of the portion of the terrain that
the user wants to view.

Data access and retrieval are enabled via an ODBC
connection to a location containing metadata related to the
objects. VxInsight uses the ODBC connection in conjunc-
tion with Structured Query Language (SQL) to provide the
user with an intuitive and powerful interface. Clicking on an
object provides details on demand (Shneiderman, 1996)

766

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

such as abstract, author, and source information in a portion
of the window reserved for those details. Queries can be
made (e.g., show all objects where ORG is like SANDIA)
using the built-in interface. Objects (e.g., documents) re-
trieved by the query are highlighted as colored markers on
the terrain. The distribution of query markers is very mean-
ingful in the context provided by the terrain with its labeling
capability, and provides clues to the analyst for further
browsing.

VxInsight allows users to spot trends over time by using
a time slider. As the user limits the time ﬁeld to a few years
and then moves the sliding time window back and forth
through time, growth and reduction in areas of interest, new
emerging areas, and bridged regions that have merged to-
gether are revealed. Visual tracking of the location and
concentration of colored query markers (corresponding to,
e.g., different companies of interest) over time using a
sliding time window can be used to track the ebb and ﬂow
of competitive advantage as represented in literature or
patent art. VxInsight can also display directional links be-
tween data objects such as citations or Web links. When the
user selects connections for display, directional links such
as citations between objects appear. These links give the
analyst detailed information about the structure of the data,
and can suggest reasons as to why some objects cluster
together while others do not.

Applications

Use of any analysis tool typically starts from one of two
points. In the ﬁrst case, one has questions to answer. Here
the analysis includes gathering of relevant data and the
attempt to ﬁnd meaningful answers from that data. In the
second case, one has data to analyze and understand. This is
more often the case with experiments from which data are
gathered. We have used VxInsight in both types of situa-
tions, but show illustrative examples of only the ﬁrst type
here because our focus in this article is on competitive
intelligence applications of domain analysis. Analysis of
genomic microarray data (Davidson, Wylie, & Boyack
2001) is an example of the second case, and will not be
explored further here.

We have performed domain analyses using VxInsight to
answer speciﬁc questions regarding many different technol-
ogies of interest to Sandia National Laboratories over the
past few years. Three examples will be given here: (1)
mapping of technology using citations from the Science
Citation Index (SCI), (2) mapping the domain space of
several institutions using the text in abstracts from multiple
bibliographic sources, and (3) mapping the structure of the
physical sciences using the citation relationships between
journals. Each of these analyses had a speciﬁc S&T purpose
within Sandia and was used to answer speciﬁc questions.
VxInsight was also used to visually present justiﬁcation for
the insights gained from the analyses to those with authority
to affect changes in S&T management.

Although three different domain analyses are presented
here, the process followed to conduct each study was the same.
First, relevant and appropriate data were procured, typically by
query to a bibliographic database. Second, an object-to-object
similarity was calculated. This step can require the use of
database functions, statistics, or other mathematical processing
depending upon the type of similarity chosen. Third, the data
were clustered using the VxOrd algorithm. Fourth, the data
were loaded into VxInsight for viewing, navigation, discovery,
and analysis.

Microsystems Domain Using Citation Mapping

Sandia has developed expertise in microsystems engi-
neering in recent years as a part of its stockpile stewardship
mission, and wanted to survey the ﬁeld to identify potential
collaborators for speciﬁc projects. To capture the essence of
what comprised the microsystems ﬁeld at the time and to
provide an appropriate seed for data extraction, relevant
technical terms were taken from a survey article on micro-
systems (Picraux & McWhorter, 1998). If a recent and
comprehensive review article such as this had not been
available, we would have consulted with experts in the ﬁeld
to construct the search term list. Proper input is essential to
the technology mapping process. Our list included over 80
terms (including, e.g., MEMS, biomimetic, microdevice,
microvalve, quantum dot, photonic crystal, etc.), and was
used to query titles and keywords from the SCI. A total of
20,923 articles from the years 1990 –1999 matched the
query terms. Of these, 13,433 articles were connected to at
least one other article in the set by citation. The citation list
was used in VxOrd to calculate both a similarity measure
(using a direct:cocitation ratio of 5:1, see Small, 1997) and
the x,y coordinates for each article, resulting in the map
shown in Figure 2.

The ﬁrst step in analysis of the microsystems map was to
understand the lay of the land. Navigation and query re-
vealed that four main technology categories populated the
landscape: quantum dots and wires; nanoscale technologies;
microtechnologies (e.g., microsystems, MEMS, and other
microcomponents); and monolayer technology. Approxi-
mately 90% of the articles in the map were directly related
to one or more of these four categories. Analysis of trends
shown by the microsystems map at a macrolevel were
identiﬁed using the time-sliding function of VxInsight. The
landscape view was limited to the articles within a 2-year
period of time. Consecutive 2-year periods were viewed,
and resulting shifts in the peaks and valleys within the
landscape were noted. For example, Figure 3 shows the
2-year periods of (a) 1994 –1995 and (b) 1998 –1999. The
peak near the top of the landscape has grown in size,
indicating more publishing activity in the later years. Ad-
ditionally, the peak label has changed from “GaAs/Self-
assembled” to “InAs/Self-assembled,” indicating a shift in
the materials used in the quantum dot technology from
GaAs to InAs. Query results shown as colored dots over the
landscape support this interpretation, and also show a shift

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

767

FIG. 2. VxInsight view of the microsystems technology landscape. Articles by Sandia authors are shown as light gray dots on the terrain.

from “grown” (black query results in Fig. 3a) to “self-
assembled” (light query results in Fig. 3b) quantum dots.

A more detailed analysis was also conducted. Queries
were made to identify the institutions doing the most
work in the microsystems ﬁeld. Additional work revealed
the number of articles from each institution in each of the
four main categories, thus indicating relative areas of
focus of various institutions. Example distributions are
given in Table 1, along with the number of articles that
do not ﬁt into any of the four main categories (i.e., the
“Other” column).

Accumulation of these results revealed differences be-
tween types of institutions as well. U.S. universities as a
whole divided their research nearly equally between the
microtechnology, quantum dots and wires, and monolayer
areas, and did slightly less work in the nanotechnology area.
By contrast, U.S. industry was heavily focused on quantum
technologies, while U.S. government laboratories focused
on quantum and monolayer research. Research by Japanese
and European industry was even more heavily focused on
quantum technologies than was research at U.S. ﬁrms. Al-
though nanotechnology work was less prevalent than the
other three categories, it had a larger overlap with the other
categories than any of the other three main categories.

A ﬁnal analysis was done to identify those institutions
whose expertise closely matches Sandia’s in speciﬁc areas.

One way to ﬁnd these types of synergies is to drill down into
small areas within the landscape and follow citation links to
and from Sandia papers (see Fig. 4). This helps identify not
only institutions, but speciﬁc researchers as potential col-
laborators, and also shows relevant prior or existing collab-
orations that have resulted in publication.

Analyses such as these where the data comes from the
SCI have obvious beneﬁts and limitations. A primary ben-
eﬁt is that the citation structure provides a defensible basis
for mapping the structure of science, and lends itself well to
detailed analysis. However, the SCI does not provide com-
plete coverage of all literature that may be relevant to a
topic of interest. Speciﬁcally, it includes few proceedings or
conference papers. Inclusion of these types of articles from
other sources should provide better coverage of a technol-
ogy area, and thus allow more accurate answers to questions
such as those listed in the introduction.

DOE Laboratories Using Text Mapping

Another area of interest to Sandia is the domain within
which it operates compared to its sister institutions, Los
Alamos National Laboratory (LANL) and Lawrence Liver-
more National Laboratory (LLNL). Every few years the
subjects of potential consolidation and duplication of effort

768

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

FIG. 3. Detail on microsystems technology landscape. (a) the 2-year period from 1994 –1995, (b) the 2-year period from 1998 –1999. Analysis of the
growth, reduction, and shifts in the landscape from the earlier time period to the later time period indicates trends in the technology area. A shift from GaAs
to InAs-related work is indicated by the two larger peaks in (b). Dot legend: black— grown (cid:4) InAs and GaAs; light—self-assembled InAs and GaAs.

seem to arise and must be answered. This study was de-
signed to show the potential overlaps and areas of differen-
tiation between the three laboratories.

The question of which data sources to use also became
important for this study. SNL, LANL, and LLNL present
work at many conferences and publish many government

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

769

TABLE 1. Distribution of articles in the four main microsystems-related categories for ﬁve institutions.

Total

Microtechnologies

Nanotechnologies

Quantum
dots/wires

Monolayers

Other

Harvard Univ.
UCSB
IBM
Sandia
Univ. Michigan

203
197
161
123
118

60
12
37
24
53

25
23
35
19
8

35
136
49
16
36

133
9
40
22
14

6
34
29
51
13

Numbers in the ﬁve category columns do not add to the total due to overlaps between the categories.

reports, which are not covered by the SCI. We felt the need
to include database sources that would include these types
of publications. A second question for this study thus was
concerned with whether or not we could effectively produce
a technology map from multiple database sources, and if the
additional databases would add information in new areas
rather than just increasing the depth of coverage in the same
areas.

Queries were made to ﬁve bibliographic databases: SCI,
Cambridge Scientiﬁc Abstracts (CSA), Engineering Index
(EI), INSPEC, and Medline, to extract all articles authored
by SNL, LANL, and LLNL during the time period 1997–
1999. The CSA source was particularly important in that it

contains documents from the National Technical Informa-
tion Service (NTIS), which is where government reports
from the three laboratories can be found. A common format
was used to combine information from each of the original
sources (see Table 2). A total of 26,362 articles were ex-
tracted from the ﬁve database sources, of which 17,927
were unique. Duplicate articles from the merged data were
eliminated by identiﬁcation of identical (or nearly identical)
abstracts. Table 3 shows that the total number of unique
articles was more than double the number of articles that
were available from the SCI alone. Thus, our goal of ob-
taining more complete and accurate coverage of the tech-
nology domain comprised by the three laboratories was met.

FIG. 4. Detailed view of the small portion of the microsystems technology landscape. Arrows indication citation with the cited paper at the arrow tip.
Highly cited articles are easily identiﬁed as those surrounded by many arrow tips.

770

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

TABLE 2. Common format for entries from different bibliographic data
sources.

Combined

INSPEC, EI, SCI

CSA

Medline

Abstract
Org
Source
Year
Type
Title
Author
Terms

AB
IN
JN
parse from PB
DT
TI
AU
DE

AB
AF
SO
PY
PT
TI
AU
DE

AB
AD
SO
DP
PT
TI
AU
MH

The choice of a data ﬁeld on which to base similarity is
very important, and should be done using a ﬁeld that has
rich and common content across all contributing data
sources. Citation structure is not common to all sources and
cannot be used. Use of citation structure for similarity
calculation is also not suitable for data that cover only a
short period of time (e.g., 3 years) due to the very low
number of citations within the set. A short list of ﬁelds
containing content potentially suitable for calculation of
similarity includes titles, terms, and abstracts. Titles are
often too short to provide any comparative content. Differ-
ent database vendors assign different sets of descriptive
terms to the same or similar articles, making terms a dubi-
ous choice for comparison (Qin, 2000).1 Thus, we chose to
base similarity on the textual content in abstracts.

Calculation of similarity values between article pairs was
done using a commercial software package, RetrievalWare
6.6 for Unix, by Convera (formerly Excalibur Technolo-
gies). RetrievalWare has a query-by-example search func-
tion, which allows the user to use any document (in our
case, the abstract) as the query. The software then looks at
all other documents in the set, ﬁnds those documents most
like the query document based on word frequency, word
location, and potential multiple meanings, and returns a list
of documents, each with a ranking score. We use this
ranking score as our similarity value, and keep the top 10
similarity values for each article for inclusion in the simi-
larity matrix. Ordination was done using the VxOrd clus-
tering algorithm, resulting in the map shown in Figure 5.

Analysis of this three-lab landscape was done using a
navigation and query process similar to that used on the
microsystems landscape. A detailed analysis (not shown
here) found that while there are pockets of activity where
two or even all three labs publish in the same ﬁeld or
collaborate, there are many more areas that differentiate the
three laboratories. For example, although all three labs do
materials work, SNL has a differentiating strength in semi-
conductor materials, LANL publishes heavily on radioac-
tive materials handling and alloys, and LLNL publishes

1 Unpublished studies on similar data drawn from multiple database
sources using a coterm similarity and VxOrd clustering show that the
articles cluster by bibliographic source rather than by similarities between
terms.

extensively on plasmas. Analysis such as this provided
answers to the ﬁrst question asked of this study.

To answer the second question, we queried the map for
different types of articles. Noyons, Moed, and Luwel (1999)
raise the issue that journals and conferences may cover
different topics. Our analysis of the three-lab landscape
shows that although articles, conference papers, and gov-
ernment publications coexist in much of the map space,
there are pockets in the landscape where one type of pub-
lication predominates (see Fig. 5). This is particularly true
near the bottom of the map where there are high concen-
trations of conference papers and government documents,
corresponding to areas such as high-energy physics and
work with radioactive substances. Although it may be ar-
gued that the DOE laboratories specialize in these areas, and
that this example is not generally applicable to all ﬁelds, it
raises the issue that specialization between journals and
conferences may occur in other ﬁelds as well. S&T man-
agement is made more robust by inclusion of all pertinent
sources of information; thus, we recommend that if S&T
decisions are to be made using detailed domain analyses as
input, multiple bibliographic sources should be included.

In addition to mapping domains based on bibliographic
sources, we have also used this text mapping process to
produce landscapes of Sandia discretionary R&D activi-
ties using proposals submitted by individual researchers.
Analysis of these data allows Sandia to identify potential
collaborations within the company (which are not always
obvious within a large research institution), and to track
the shift in internal R&D spending in different technical
areas from year to year. Inclusion of corporate goals and
line-of-sight descriptions in the landscape allow manage-
ment to correlate and align investment with corporate
goals.

Journal Mapping

One of Sandia’s ongoing efforts is an extensive univer-
sity collaboration program. This includes not only speciﬁc
research collaborations, but also events such as a Dean’s
Day, where deans from many engineering schools around
the United States convene on an annual basis. To promote
detailed discussions between Sandia administrative staff
and researchers and their counterparts from universities, we

TABLE 3. Number of articles kept from each data source in combined
data set.

Source

Number of articles

Number unique

% Unique

SCI
CSA
EI
INSPEC
Medline
Duplicates
Total

8,318
5,797
3,812
8,028
407

26,362

4,542
2,783
1,055
3,719
54
5,774
17,927

54.6%
48.0%
27.6%
46.3%
13.3%

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

771

FIG. 5. VxInsight view of the three lab technology landscape from 1997–1999. Dot legend: dark gray—journal articles; light gray— conference papers;
white— government documents (primarily from NTIS).

have produced a map of the physical sciences based on the
3,000 journals (4.7 million articles) in the physical sciences
subset of the SCI from 1981–1996.

The similarity between journals was deﬁned as (A cites
B) (cid:4) (B cites A), where A and B are any two journals.
Normalization, such as that in cosine- or Jaccard-type sim-
ilarities, was not used. Ignoring normalization naturally
provides higher weights to interactions between the larger,
more heavily referenced journals, thus producing a map
where the large journals form clusters, and the smaller
journals agglomerate to the large journals they are most like.
Ordination of journals was done using the VxOrd algorithm.
The resulting landscape (see Fig. 6) shows that Physics
occupies a central position relative to other disciplines
within the physical sciences. Clusters of engineering, math-
ematics, computing, and materials science journals all sur-
round physics with strong links to physics journals. Several
chemistry disciplines occupy the ridge on the right edge of
the map and have strong connections back to physics as well
as to materials and geology. At the macrolevel this map has
much in common with the physical sciences portion of the
map generated by Bassecoulard and Zitt (1999).

A close-up view of a cluster in the center of the astro-
physics peak (see Fig. 6b) shows strong relationships (blue
lines) between major journals in that ﬁeld. It is interesting
that Nature appears in this cluster, although it is a multidis-
ciplinary journal. In this map where life sciences are not
included, Nature’s strongest links are to well-known astro-
physics journals. In a map including the life sciences, one
might expect links between biology and microbiology jour-
nals and Nature to outweigh those from astrophysics. Dif-
ﬁculties associated with clustering multidisciplinary jour-
nals have been enumerated by Bassecoulard and Zitt (1999).
Sandia has used this map of the physical and engineering
sciences to both qualitatively and quantitatively compare
the output of other research institutions to ourselves in
different disciplines. A query for journals published in by
Sandia, and for those published in by, for instance, Harvard
University, shows the relative emphases placed by each
institution in different disciplines. Counting the number of
articles by institution in each cluster of journals allow us to
quantify our qualitative observations. Both overlapping em-
phases and complementary emphases are important infor-
mation when pursuing strategic partnerships.

772

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

FIG. 6. Landscape of the physical sciences based on the journals in the ISI physical sciences database from 1981–1995. Inset: detail on the Astrophysics
cluster from the large map. Strong links between individual journals in the cluster are shown as lines.

Conclusions

The following general and speciﬁc conclusions about the
VxInsight tool and analysis environment have been reached
as a result of many detailed studies using the tool.

(1) The nonexpert who has achieved some proﬁciency us-
ing VxInsight can quickly discover general characteris-
tics in a technology domain.

(2) If a detailed domain analysis of a competitive nature is
required, interaction with subject matter experts is es-
sential for proper search term formulation and analysis
of the domain map. Interaction with bibliographic data
using VxInsight can aid the expert to see trends in
technology domains.

(3) Use of a similarity measure based on a common number
of descriptive terms does not work well for an article set
built from two or more bibliographic sources due to
differences in the thesauri and term sets used by the
different data vendors.

(4) Data from multiple bibliographic sources provide much
better coverage of a technology area than does one
source, and can be merged with good success to pro-
duce meaningful domain maps. In addition, some sub-

technologies can be completely overlooked if only one
data source is used.

(5) A similarity measure based on common textual material
in abstracts works very well on merged databases and
produces useful and navigable domain maps. More ef-
ﬁcient and precise textual analysis techniques would aid
in producing more robust domain maps.

In a larger context, visualization tools, such as VxInsight,
are becoming crucial to science and technology manage-
ment in the context of textual data mining, roadmapping,
and forecasting. Technical experts have always been, and
still are, extremely crucial to this process. Computerized
mapping methods may never replace the human analytical
capability.

The Naval Research Laboratory has sponsored research
over many years aimed at using textual sources in their S&T
management process, including roadmapping and the iden-
from
of
tiﬁcation
Losiewicz et al. (2000):

technologies. Quoting

promising

The FY98 experience showed conclusively that high-quality
data mining requires the close involvement of technical

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

773

domain expert(s) in information retrieval, phrase frequency
and proximity analyses, and presentation. Multiple perspec-
tives are often needed to detect data anomalies . . . TDM
[textual data mining] cannot realize its full potential in S&T
management if used only sporadically—it must become an
integral part of the S&T sponsor’s business operations.
Because of the learning curve, long-term involvement of
experts with data mining experience in a particular topic
area is desirable.

Development of a long-term capability for S&T manage-
ment, including roadmapping, and forecasting, while not an
easy process, will prove to be increasingly valuable as we
proceed in this information and technology-rich age. Visu-
alization will be an integral and essential part of these
efforts.

References

Bassecoulard, E., & Zitt, M. (1999). Indicators in a research institute: A
multi-level classiﬁcation of scientiﬁc journals. Scientometrics, 44, 323–
245.

Beck, D.F., Boyack, K.W., Bray, O.H., & Siemens, W.D. (1999). Land-
scapes, games, and maps for technology planning. CHEMTECH, 29(6),
8 –16.

Bo¨rner, K. (2000). Visible threads: A smart VR interface to digital librar-
ies. Proceedings of the IST/SPIE 12th annual symposium: Electronic
imaging 2000, visual data exploration & analysis, San Jose, CA, Jan.
2000.

Boyack, K.W., Wylie, B.N., Davidson, G.S., & Johnson, D.K. (2000).
Analysis of patent databases using VxInsight. Proceedings of New
Paradigms
in Information Visualization and Manipulation 2000,
McLean, VA, November 10, 2000, ACM.

Chen, C. (1999). Visualising semantic spaces and author co-citation net-
works in digital libraries. Information Processing and Management, 35,
401– 420.

Chen, C., Paul, R.J., & O’Keefe, B. (2001). Fitting the jigsaw of citation:
Information visualization in domain analysis. Journal of the American
Society for Information Science and Technology, 52(4), 315–330.
Davidson, G.S., Hendrickson, B., Johnson, D.K., Meyers, C.E., & Wylie,
B.N. (1998). Knowledge mining with VxInsight: Discovery through
interaction. Journal of Intelligent Information Systems, 11, 259 –285.
Davidson, G.S., Wylie, B.N., & Boyack, K.W. (2001). Cluster stability and
the use of noise in interpretation of clustering. Proceedings IEEE Infor-
mation Visualization 2001, 23–30.

Fox, K L., Frieder, O., Knepper, M.M., & Snowberg, E.J. (1999). SEN-
TINEL: A multiple engine information retrieval and visualization sys-
tem. Journal of the American Society for Information Science, 50(7),
616 – 625.

Hetzler, B., Whitney, P., Martucci, L., & Thomas, J. (1998). Multi-faceted
insight through interoperable visual information analysis paradigms.
Proceedings of IEEE Information Visualization ’98 (pp. 137–144).

Hjorland, B., & Albrechtsen, H. (1995). Toward a new horizon in infor-
mation science: Domain analysis. Journal of the American Society for
Information Science, 46(6), 400 – 425.

Honkela, T., Kaski, S., Kohonen, T., & Lagus, K. (1998). Self-organizing
maps of very large document collections: Justiﬁcation for the WEBSOM
method. In I. Balderjahn, R. Mathar, & M. Schader (Eds.), Classiﬁca-
tion, data analysis, and data highways. Berlin: Springer.

Kostoff, R.N., Eberhart, H.J., & Toothman, D.R. (1999). Hypersonic and
supersonic ﬂow roadmaps using bibliometrics and database tomography.
Journal of the American Society for Information Science, 50(5), 427–
447.

Landauer, T.K., Foltz, P.W., & Laham, D. (1998) Introduction to latent

semantic analysis. Discourse Processes, 25, 259 –284.

Leydesdorff, L. (1994). The generation of aggregated journal-journal cita-
tion maps on the basis of the CD-ROM version of the Science Citation
Index. Scientometrics, 31, 59 – 84.

Losiewicz, P., Oard, D.W., & Kostoff, R.N. (2000). Textual data mining to
support science and technology management. Journal of Intelligent
Information Systems, 15(2), 99 –119.

McCain, K.W. (1998). Neural networks research in context: A longitudinal
journal cocitation analysis of an emerging interdisciplinary ﬁeld. Scien-
tometrics, 41, 389 – 410.

Nederhof, A.J., & Van Wijk, E. (1997). Mapping the social and behavioral
sciences world-wide: Use of maps in portfolio analysis of national
research efforts. Scientometrics, 40, 273–276.

Newman, M.E.J. (2001). Scientiﬁc collaboration networks. I. Network
construction and fundamental results. Physical Review E, 64, paper
number 016131.

Noyons, E.C.M., & Van Raan, A.F.J. (1998). Advanced mapping of

science and technology. Scientometrics, 41, 61– 67.

Noyons, E.C.M., Moed, H.F., & Luwel, M. (1999). Combining mapping
and citation analysis for evaluative bibliometric purposes: A bibliomet-
ric study. Journal of the American Society for Information Science,
50(2), 115–131.

Picraux, S.T., & McWhorter, P.J. (1998). The broad sweep of integrated

microsystems. IEEE Spectrum, 35(12), 24 –33.

Qin, J. (2000). Semantic similarities between a keyword database and a
controlled vocabulary database: An investigation in the antibiotic resis-
tance literature. Journal of the American Society for Information Sci-
ence, 51(2), 166 –180.

Shneiderman, B (1996). The eyes have it: A task by data type taxonomy for
information visualizations. In Proc. IEEE Symp. Visual Languages ’96
IEEE.

Small, H. (1997). Update on science mapping: Creating large document

spaces. Scientometrics, 38, 275–293.

Small, H. (1999). Visualizing science by citation mapping. Journal of the

American Society for Information Science, 50(9), 799 – 813.

Spasser, M.A. (1997). Mapping the terrain of pharmacy: Co-classiﬁcation
analysis of the International Pharmaceutical Abstracts database. Scien-
tometrics, 39, 77–97.

White, H.D., & McCain, K.W. (1998) Visualizing a discipline: An author
co-citation analysis of information science, 1972–1995. Journal of the
American Society for Information Science, 49(4), 327–355.

Wise, J.A. (1999). The ecological approach to text visualization. Journal of
the American Society for Information Science, 50(13), 1224 –1233.

774

JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION SCIENCE AND TECHNOLOGY—July 2002

