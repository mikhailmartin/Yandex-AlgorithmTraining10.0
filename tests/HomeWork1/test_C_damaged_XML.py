import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.C_damaged_XML import (
    Solver,
    Tag,
    TagType,
    # синтаксические ошибки
    NoLabError,
    ImpossibleLabError,
    RabWithEmptyContentError,
    UnexpectedLabError,
    UnexpectedSlashError,
    NoRabError,
    # структурные ошибки
    ExtraCloseError,
    MissMatchError,
    UnclosedError,
)


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        param(
            "<a><a><b></b></c></c>",
            [
                Tag(TagType.OPEN, "a"),
                Tag(TagType.OPEN, "a"),
                Tag(TagType.OPEN, "b"),
                Tag(TagType.CLOSE, "b"),
                Tag(TagType.CLOSE, "c"),
                Tag(TagType.CLOSE, "c"),
            ],
        ),
    ],
)
def test_parse_tags(string, expected):
    assert Solver._parse_tags(list(string)) == expected


@pytest.mark.parametrize(
    ("string", "expected_error", "pos"),
    [
        param("a", NoLabError, 0, id="custom1"),
        param("<a>a", NoLabError, 3, id="custom2"),
        param("<a></a>a", NoLabError, 7, id="custom3"),
        param("<<", ImpossibleLabError, 1, id="custom4"),
        param("<a><<", ImpossibleLabError, 4, id="custom5"),
        param("<a></a><<", ImpossibleLabError, 8, id="custom6"),
        param("<>", RabWithEmptyContentError, 1, id="custom7"),
        param("</>", RabWithEmptyContentError, 2, id="custom8"),
        param("<a<", UnexpectedLabError, 2, id="custom9"),
        # замены < в <a> или </a>
        param("/a>", NoLabError, 0, id="custom10"),
        param("aa>", NoLabError, 0, id="custom11"),
        param(">a>", NoLabError, 0, id="custom12"),
        param("//a>", NoLabError, 0, id="custom13"),
        param("a/a>", NoLabError, 0, id="custom14"),
        param(">/a>", NoLabError, 0, id="custom15"),
        # замены / в </a>
        param("<<a>", ImpossibleLabError, 1, id="custom16"),
        # param("<aa>")
        param("<>a>", RabWithEmptyContentError, 1, id="custom17"),
        # замены a в <a> или </a>
        param("<<>", ImpossibleLabError, 1, id="custom18"),
        param("</>", RabWithEmptyContentError, 2, id="custom19"),
        param("<>>", RabWithEmptyContentError, 1, id="custom20"),
        param("</<>", UnexpectedLabError, 2, id="custom21"),
        param("<//>", UnexpectedSlashError, 2, id="custom22"),
        param("</>>", RabWithEmptyContentError, 2, id="custom23"),
        # замены > в <a> или </a>
        param("<a<", UnexpectedLabError, 2, id="custom24"),
        param("<a/", UnexpectedSlashError, 2, id="custom25"),
        param("<aa", NoRabError, 2, id="custom26"),
        param("</a<", UnexpectedLabError, 3, id="custom27"),
        param("</a/", UnexpectedSlashError, 3, id="custom28"),
        param("</aa", NoRabError, 3, id="custom29"),
    ],
)
def test_parse_tags_with_errors(string, expected_error, pos):
    with pytest.raises(expected_error) as exec_info:
        Solver._parse_tags(list(string))
        assert exec_info.value.pos == pos


@pytest.mark.parametrize(
    "string",
    [
        param("<a></a>", id="custom1"),
    ],
)
def test__is_valid_xml(string):
    tags = Solver._parse_tags(list(string))
    assert Solver._is_valid_xml(tags) == True


@pytest.mark.parametrize(
    ("string", "expected_error"),
    [
        param("</a><a>", ExtraCloseError, id="custom2"),
        param("<a>", UnclosedError, id="custom3"),
        param("</a>", ExtraCloseError, id="custom4"),
        param("<a></b>", MissMatchError, id="custom5"),
        param("<a><aa>", UnclosedError, id="custom6"),
    ],
)
def test__is_valid_xml_errors(string, expected_error):
    tags = Solver._parse_tags(list(string))
    with pytest.raises(expected_error):
        Solver._is_valid_xml(tags)


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["/a></a>"], "<a></a>", id="custom1"),
        param(["<a>//a>"], "<a></a>", id="custom2"),
        param(["aa></a>"], "<a></a>", id="custom3"),
        param(["<a>a/a>"], "<a></a>", id="custom4"),
        param([">a></a>"], "<a></a>", id="custom5"),
        param(["<a>>/a>"], "<a></a>", id="custom6"),
        # ======================================================================
        param(["<a><<a>"], "<a></a>", id="custom7"),
        param(["<a><aa>"], "<a></a>", id="example2"),
        param(["<a><>a>"], "<a></a>", id="example3"),
        param(["<<></a>"], "<a></a>", id="custom8"),
        param(["<a></<>"], "<a></a>", id="custom9"),
        param(["</></a>"], "<a></a>", id="custom10"),
        param(["<a><//>"], "<a></a>", id="custom11"),
        param(["<>></a>"], "<a></a>", id="custom12"),
        param(["<a></>>"], "<a></a>", id="custom13"),
        param(["<a<</a>"], "<a></a>", id="custom14"),
        param(["<a></a<"], "<a></a>", id="custom15"),
        param(["<a/</a>"], "<a></a>", id="example4"),
        param(["<a></a/"], "<a></a>", id="custom16"),
        param(["<aa</a>"], "<a></a>", id="custom17"),
        param(["<a></aa"], "<a></a>", id="custom18"),
        param(["<a></b>"], "<b></b>", id="example1"),
        param(
            ["<v><tbvh></tbvh><o><kksav></kksav></o><ypya></ypya><saed></saed><urgps></urgps></v><bdf><kgls><h></h></kgls><af><yv></yv></af><bxf></bxf></bdf><is></is><od></od<"],
            "<v><tbvh></tbvh><o><kksav></kksav></o><ypya></ypya><saed></saed><urgps></urgps></v><bdf><kgls><h></h></kgls><af><yv></yv></af><bxf></bxf></bdf><is></is><od></od>",
            id="test12",
        ),
        param(
            ["<qdb><tdhwb><j><zkrp><mbd></mbd></zkrp><aryg></aryg></j><ysygr></ysygr><h></h></tdhwb><p></p><stb><mc><xbax></xbax><ti><zbmaf></zbmaf></ti><lnsfu></lnsfu></mc><vm></vm><snh></snh></stb><xyvb></xyvb><sxuv><vep></vep><zmcsj></zmcsj></sxuv><jcidc></jcidc></qdb><l><yt><ux><j><jzxrs></jzxrs><yxycd><ddpn></ddpn></yxycd><px></px></j><cko></cko><zb></zb><bnw></bnw></ux><hra><k><pwtf></pwtf></k><ylpbs><m></m></ylpbs><hlstw></hlstw></hra><j><rlrq><xpcmz></xpcmz><wdac></wdac></rlrq><bomrv></bomrv></j><gbho></gbho><g><bs></bs></g><g></g></yt><vxyd><hoot><fc><n></n></fc><byvu><mtvte><itwxg></itwxg></mtvte><gk></gk></byvu><vskd></vskd><o></o></hoot><jsrpp></jsrpp></vxyd><nph><fjvom></fjvom><utgdy><czhv></czhv></utgdy><wh></wh></nph><tggki><vhphp></vhphp></tggki><it><wit></l><u><keegk><zbw><huo><wpr></wpr><fpdes></fpdes><lh></lh></huo><pp></pp></zbw><cxect></cxect><ov></ov></keegk><ky></ky><fi></fi></u><n><g></g><c></c></n><mp></mp><irphi></irphi>"],
            "<qdb><tdhwb><j><zkrp><mbd></mbd></zkrp><aryg></aryg></j><ysygr></ysygr><h></h></tdhwb><p></p><stb><mc><xbax></xbax><ti><zbmaf></zbmaf></ti><lnsfu></lnsfu></mc><vm></vm><snh></snh></stb><xyvb></xyvb><sxuv><vep></vep><zmcsj></zmcsj></sxuv><jcidc></jcidc></qdb><l><yt><ux><j><jzxrs></jzxrs><yxycd><ddpn></ddpn></yxycd><px></px></j><cko></cko><zb></zb><bnw></bnw></ux><hra><k><pwtf></pwtf></k><ylpbs><m></m></ylpbs><hlstw></hlstw></hra><j><rlrq><xpcmz></xpcmz><wdac></wdac></rlrq><bomrv></bomrv></j><gbho></gbho><g><bs></bs></g><g></g></yt><vxyd><hoot><fc><n></n></fc><byvu><mtvte><itwxg></itwxg></mtvte><gk></gk></byvu><vskd></vskd><o></o></hoot><jsrpp></jsrpp></vxyd><nph><fjvom></fjvom><utgdy><czhv></czhv></utgdy><wh></wh></nph><tggki><vhphp></vhphp></tggki><it></it></l><u><keegk><zbw><huo><wpr></wpr><fpdes></fpdes><lh></lh></huo><pp></pp></zbw><cxect></cxect><ov></ov></keegk><ky></ky><fi></fi></u><n><g></g><c></c></n><mp></mp><irphi></irphi>",
            id="test15",
        ),
        param(
            ["<fjsm><mb><wvs><zwcac></zwcac><pz></pz></wvs><e><ai></ai><iiilx></iiilx><fnko></fnko></e><zjam></zjam></mb><lh><c></c><m></m></lh><kbbbl><mnb><gx><d><vnyto></vnyto></d><tc></tc><lobb></lobb><krj></krj><ci></ci></gx><hptid><rjc></rjc><jw><wvck></wvck></jw><sheyv></sheyv><zl></zl></hptid><wy></wy><lczx><q></q></lczx><ok></ok></mnb><a></a><sw></sw><r></r></kbbbl><fjrn><ixnq><x><deoft></deoft><mhe></mhe><ols></ols></x><od></od><hlfo></hlfo></ixnq><b></b><l></l></fjrn><yezfq></yezfq><thwc><a><ulbk></ulbk></a><z></z></thwc><ddgmm></ddgmm></fjsm><f><gvvm></gvvm><zsnfd></zsnfd></f><bkjhs><epr></epr></bkjhs><hzu></hzu><grnn><q><m></m><t><mtg></mtg></t><ew></e<></q><ojeoh></ojeoh></grnn><hwbc></hwbc><xlgf></xlgf>"],
            "<fjsm><mb><wvs><zwcac></zwcac><pz></pz></wvs><e><ai></ai><iiilx></iiilx><fnko></fnko></e><zjam></zjam></mb><lh><c></c><m></m></lh><kbbbl><mnb><gx><d><vnyto></vnyto></d><tc></tc><lobb></lobb><krj></krj><ci></ci></gx><hptid><rjc></rjc><jw><wvck></wvck></jw><sheyv></sheyv><zl></zl></hptid><wy></wy><lczx><q></q></lczx><ok></ok></mnb><a></a><sw></sw><r></r></kbbbl><fjrn><ixnq><x><deoft></deoft><mhe></mhe><ols></ols></x><od></od><hlfo></hlfo></ixnq><b></b><l></l></fjrn><yezfq></yezfq><thwc><a><ulbk></ulbk></a><z></z></thwc><ddgmm></ddgmm></fjsm><f><gvvm></gvvm><zsnfd></zsnfd></f><bkjhs><epr></epr></bkjhs><hzu></hzu><grnn><q><m></m><t><mtg></mtg></t><ew></ew></q><ojeoh></ojeoh></grnn><hwbc></hwbc><xlgf></xlgf>",
            id="test16",
        ),
        param(
            ["<v><tsl><rsbd><mg><le><etlf></etlf><jhd></jhd></le><fcvo></fcvo></mg><f><pjay></pjay><di></di></f><jas></jas><yr></yr><gs></gs></rsbd><n><rvlmp></rvlmp></n><p></p></tsl><wt><b></b><lilxi><cjejt></cjejt></li>xi><pypd></pypd></wt><g></g></v><mzv><m></m><phldt></phldt></mzv><si></si><jcx></jcx><vlvgd></vlvgd>"],
            "<v><tsl><rsbd><mg><le><etlf></etlf><jhd></jhd></le><fcvo></fcvo></mg><f><pjay></pjay><di></di></f><jas></jas><yr></yr><gs></gs></rsbd><n><rvlmp></rvlmp></n><p></p></tsl><wt><b></b><lilxi><cjejt></cjejt></lilxi><pypd></pypd></wt><g></g></v><mzv><m></m><phldt></phldt></mzv><si></si><jcx></jcx><vlvgd></vlvgd>",
            id="test17",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
