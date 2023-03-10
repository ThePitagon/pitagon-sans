## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[19] PitagonSans-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 580 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 668:
less

Width = 638:
equal

Width = 660:
greater

Width = 635:
logicalnot

Width = 585:
plusminus

Width = 534:
multiply

Width = 628:
divide

Width = 583:
minus

Width = 636:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,503.0>--<142.0,506.0>> -> L<<142.0,506.0>--<447.0,728.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> 

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* section (U+00A7): B<<157.5,435.0>-<181.0,440.0>-<200.0,440.0>>/B<<200.0,440.0>-<188.0,441.0>-<171.0,453.5>> = 4.763641690726143 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* a (U+0061): L<<519.0,342.0>--<518.0,105.0>>

	* aacute (U+00E1): L<<519.0,342.0>--<518.0,105.0>>

	* abreve (U+0103): L<<519.0,342.0>--<518.0,105.0>>

	* acircumflex (U+00E2): L<<519.0,342.0>--<518.0,105.0>>

	* adieresis (U+00E4): L<<519.0,342.0>--<518.0,105.0>>

	* agrave (U+00E0): L<<519.0,342.0>--<518.0,105.0>>

	* amacron (U+0101): L<<519.0,342.0>--<518.0,105.0>>

	* aogonek (U+0105): L<<519.0,342.0>--<518.0,105.0>>

	* aring (U+00E5): L<<519.0,342.0>--<518.0,105.0>>

	* aringacute (U+01FB): L<<519.0,342.0>--<518.0,105.0>>

	* atilde (U+00E3): L<<519.0,342.0>--<518.0,105.0>>

	* dotlessi (U+0131): L<<242.0,499.0>--<244.0,0.0>>

	* fi (U+FB01): L<<646.0,499.0>--<648.0,0.0>>

	* h (U+0068): L<<243.0,361.0>--<240.0,0.0>>

	* hbar (U+0127): L<<243.0,361.0>--<240.0,0.0>>

	* hcircumflex (U+0125): L<<243.0,361.0>--<240.0,0.0>>

	* i (U+0069): L<<244.0,499.0>--<246.0,0.0>>

	* ibreve (U+012D): L<<242.0,499.0>--<244.0,0.0>>

	* ij (U+0133): L<<244.0,499.0>--<246.0,0.0>>

	* ij (U+0133): L<<563.0,509.0>--<565.0,7.0>>

	* iogonek (U+012F): L<<244.0,499.0>--<246.0,1.0>>

	* itilde (U+0129): L<<242.0,499.0>--<244.0,0.0>>

	* j (U+006A): L<<257.0,509.0>--<259.0,7.0>>

	* k (U+006B): L<<241.0,196.0>--<240.0,0.0>>

	* k (U+006B): L<<243.0,700.0>--<241.0,326.0>>

	* s (U+0073): L<<439.0,474.0>--<440.0,339.0>>

	* sacute (U+015B): L<<439.0,474.0>--<440.0,339.0>>

	* scaron (U+0161): L<<439.0,474.0>--<440.0,339.0>>

	* scedilla (U+015F): L<<439.0,474.0>--<440.0,339.0>>

	* scircumflex (U+015D): L<<439.0,474.0>--<440.0,339.0>>

	* uni01C8 (U+01C8): L<<825.0,509.0>--<827.0,7.0>>

	* uni01C9 (U+01C9): L<<557.0,509.0>--<559.0,7.0>>

	* uni01CB (U+01CB): L<<982.0,509.0>--<984.0,7.0>>

	* uni01CC (U+01CC): L<<883.0,509.0>--<885.0,7.0>>

	* uni01CE (U+01CE): L<<519.0,342.0>--<518.0,105.0>>

	* uni01D0 (U+01D0): L<<242.0,499.0>--<244.0,0.0>>

	* uni0201 (U+0201): L<<519.0,342.0>--<518.0,105.0>>

	* uni0203 (U+0203): L<<519.0,342.0>--<518.0,105.0>>

	* uni0209 (U+0209): L<<242.0,499.0>--<244.0,0.0>>

	* uni020B (U+020B): L<<242.0,499.0>--<244.0,0.0>>

	* uni0219 (U+0219): L<<439.0,474.0>--<440.0,339.0>>

	* uni1E2B (U+1E2B): L<<243.0,361.0>--<240.0,0.0>>

	* uni1E2F (U+1E2F): L<<242.0,499.0>--<244.0,0.0>>

	* uni1E61 (U+1E61): L<<439.0,474.0>--<440.0,339.0>>

	* uni1E63 (U+1E63): L<<439.0,474.0>--<440.0,339.0>>

	* uni1E65 (U+1E65): L<<439.0,474.0>--<440.0,339.0>>

	* uni1E67 (U+1E67): L<<439.0,474.0>--<440.0,339.0>>

	* uni1E69 (U+1E69): L<<439.0,474.0>--<440.0,339.0>>

	* uni1E9E (U+1E9E): L<<264.0,409.0>--<263.0,0.0>>

	* uni1EA1 (U+1EA1): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA3 (U+1EA3): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA5 (U+1EA5): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA7 (U+1EA7): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA9 (U+1EA9): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EAB (U+1EAB): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EAD (U+1EAD): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EAF (U+1EAF): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EB1 (U+1EB1): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EB3 (U+1EB3): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EB5 (U+1EB5): L<<519.0,342.0>--<518.0,105.0>> 

	* uni1EB7 (U+1EB7): L<<519.0,342.0>--<518.0,105.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[18] PitagonSans-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 572 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 662:
less

Width = 638:
equal

Width = 652:
greater

Width = 626:
logicalnot

Width = 585:
plusminus

Width = 497:
multiply

Width = 628:
divide

Width = 571:
minus

Width = 619:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* iogonek (U+012F): L<<183.0,0.0>--<183.0,0.0>> -> L<<183.0,0.0>--<183.0,0.0>>

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<447.0,729.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> 

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* V (U+0056): L<<527.0,666.0>--<643.0,667.0>>

	* a (U+0061): L<<488.0,346.0>--<487.0,106.0>>

	* aacute (U+00E1): L<<488.0,346.0>--<487.0,106.0>>

	* abreve (U+0103): L<<488.0,346.0>--<487.0,106.0>>

	* acircumflex (U+00E2): L<<488.0,346.0>--<487.0,106.0>>

	* adieresis (U+00E4): L<<488.0,346.0>--<487.0,106.0>>

	* agrave (U+00E0): L<<488.0,346.0>--<487.0,106.0>>

	* amacron (U+0101): L<<488.0,346.0>--<487.0,106.0>>

	* aogonek (U+0105): L<<488.0,346.0>--<487.0,106.0>>

	* aring (U+00E5): L<<488.0,346.0>--<487.0,106.0>>

	* aringacute (U+01FB): L<<488.0,346.0>--<487.0,106.0>>

	* atilde (U+00E3): L<<488.0,346.0>--<487.0,106.0>>

	* dotlessi (U+0131): L<<179.0,499.0>--<180.0,0.0>>

	* fi (U+FB01): L<<550.0,499.0>--<551.0,0.0>>

	* h (U+0068): L<<179.0,390.0>--<178.0,0.0>>

	* hbar (U+0127): L<<179.0,390.0>--<178.0,0.0>>

	* hcircumflex (U+0125): L<<179.0,390.0>--<178.0,0.0>>

	* i (U+0069): L<<182.0,499.0>--<183.0,0.0>>

	* ibreve (U+012D): L<<179.0,499.0>--<180.0,0.0>>

	* ij (U+0133): L<<182.0,499.0>--<183.0,0.0>>

	* ij (U+0133): L<<466.0,502.0>--<467.0,-18.0>>

	* iogonek (U+012F): L<<182.0,499.0>--<183.0,0.0>>

	* itilde (U+0129): L<<179.0,499.0>--<180.0,0.0>>

	* j (U+006A): L<<206.0,502.0>--<207.0,-18.0>>

	* k (U+006B): L<<179.0,225.0>--<178.0,0.0>>

	* uni01C8 (U+01C8): L<<743.0,502.0>--<744.0,-18.0>>

	* uni01C9 (U+01C9): L<<458.0,502.0>--<459.0,-18.0>>

	* uni01CB (U+01CB): L<<929.0,502.0>--<930.0,-18.0>>

	* uni01CC (U+01CC): L<<792.0,502.0>--<793.0,-18.0>>

	* uni01CE (U+01CE): L<<488.0,346.0>--<487.0,106.0>>

	* uni01D0 (U+01D0): L<<179.0,499.0>--<180.0,0.0>>

	* uni0201 (U+0201): L<<488.0,346.0>--<487.0,106.0>>

	* uni0203 (U+0203): L<<488.0,346.0>--<487.0,106.0>>

	* uni0209 (U+0209): L<<179.0,499.0>--<180.0,0.0>>

	* uni020B (U+020B): L<<179.0,499.0>--<180.0,0.0>>

	* uni1E2B (U+1E2B): L<<179.0,390.0>--<178.0,0.0>>

	* uni1E2F (U+1E2F): L<<179.0,499.0>--<180.0,0.0>>

	* uni1EA1 (U+1EA1): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA3 (U+1EA3): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA5 (U+1EA5): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA7 (U+1EA7): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA9 (U+1EA9): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EAB (U+1EAB): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EAD (U+1EAD): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EAF (U+1EAF): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EB1 (U+1EB1): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EB3 (U+1EB3): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EB5 (U+1EB5): L<<488.0,346.0>--<487.0,106.0>> 

	* uni1EB7 (U+1EB7): L<<488.0,346.0>--<487.0,106.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[17] PitagonSans-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 611 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 660:
less

Width = 638:
equal

Width = 649:
greater

Width = 622:
logicalnot

Width = 585:
plusminus

Width = 481:
multiply

Width = 628:
divide

Width = 566:
minus

Width = 568:
lessequal, greaterequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> 

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[19] PitagonSans-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 576 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 666:
less

Width = 638:
equal

Width = 657:
greater

Width = 631:
logicalnot

Width = 585:
plusminus

Width = 518:
multiply

Width = 628:
divide

Width = 578:
minus

Width = 629:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<542.0,728.0>--<848.0,506.0>> -> L<<848.0,506.0>--<851.0,504.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> 

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Q (U+0051): B<<210.0,332.0>-<210.0,262.0>-<221.0,214.0>>/L<<221.0,214.0>--<221.0,217.0>> = 12.907408671265848 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* V (U+0056): L<<524.0,666.0>--<696.0,667.0>>

	* a (U+0061): L<<506.0,344.0>--<505.0,105.0>>

	* aacute (U+00E1): L<<506.0,344.0>--<505.0,105.0>>

	* abreve (U+0103): L<<506.0,344.0>--<505.0,105.0>>

	* acircumflex (U+00E2): L<<506.0,344.0>--<505.0,105.0>>

	* adieresis (U+00E4): L<<506.0,344.0>--<505.0,105.0>>

	* agrave (U+00E0): L<<506.0,344.0>--<505.0,105.0>>

	* amacron (U+0101): L<<506.0,344.0>--<505.0,105.0>>

	* aogonek (U+0105): L<<506.0,344.0>--<505.0,105.0>>

	* aring (U+00E5): L<<506.0,344.0>--<505.0,105.0>>

	* aringacute (U+01FB): L<<506.0,344.0>--<505.0,105.0>>

	* atilde (U+00E3): L<<506.0,344.0>--<505.0,105.0>>

	* dotlessi (U+0131): L<<215.0,499.0>--<216.0,0.0>>

	* fi (U+FB01): L<<606.0,499.0>--<607.0,0.0>>

	* h (U+0068): L<<216.0,373.0>--<214.0,0.0>>

	* hbar (U+0127): L<<216.0,373.0>--<214.0,0.0>>

	* hcircumflex (U+0125): L<<216.0,373.0>--<214.0,0.0>>

	* i (U+0069): L<<218.0,499.0>--<219.0,0.0>>

	* ibreve (U+012D): L<<215.0,499.0>--<216.0,0.0>>

	* ij (U+0133): L<<218.0,499.0>--<219.0,0.0>>

	* ij (U+0133): L<<521.0,506.0>--<523.0,-4.0>>

	* iogonek (U+012F): L<<218.0,499.0>--<219.0,1.0>>

	* itilde (U+0129): L<<215.0,499.0>--<216.0,0.0>>

	* j (U+006A): L<<235.0,506.0>--<237.0,-4.0>>

	* k (U+006B): L<<216.0,697.0>--<215.0,319.0>>

	* uni01C8 (U+01C8): L<<790.0,506.0>--<792.0,-4.0>>

	* uni01C9 (U+01C9): L<<515.0,506.0>--<517.0,-4.0>>

	* uni01CB (U+01CB): L<<959.0,506.0>--<961.0,-4.0>>

	* uni01CC (U+01CC): L<<844.0,506.0>--<846.0,-4.0>>

	* uni01CE (U+01CE): L<<506.0,344.0>--<505.0,105.0>>

	* uni01D0 (U+01D0): L<<215.0,499.0>--<216.0,0.0>>

	* uni0201 (U+0201): L<<506.0,344.0>--<505.0,105.0>>

	* uni0203 (U+0203): L<<506.0,344.0>--<505.0,105.0>>

	* uni0209 (U+0209): L<<215.0,499.0>--<216.0,0.0>>

	* uni020B (U+020B): L<<215.0,499.0>--<216.0,0.0>>

	* uni1E2B (U+1E2B): L<<216.0,373.0>--<214.0,0.0>>

	* uni1E2F (U+1E2F): L<<215.0,499.0>--<216.0,0.0>>

	* uni1E9E (U+1E9E): L<<232.0,425.0>--<231.0,0.0>>

	* uni1EA1 (U+1EA1): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA3 (U+1EA3): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA5 (U+1EA5): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA7 (U+1EA7): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA9 (U+1EA9): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EAB (U+1EAB): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EAD (U+1EAD): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EAF (U+1EAF): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EB1 (U+1EB1): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EB3 (U+1EB3): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EB5 (U+1EB5): L<<506.0,344.0>--<505.0,105.0>> 

	* uni1EB7 (U+1EB7): L<<506.0,344.0>--<505.0,105.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[19] PitagonSans-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 574 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 664:
less

Width = 638:
equal

Width = 655:
greater

Width = 629:
logicalnot

Width = 585:
plusminus

Width = 508:
multiply

Width = 628:
divide

Width = 575:
minus

Width = 624:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<447.0,729.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> 

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* V (U+0056): L<<526.0,666.0>--<670.0,667.0>>

	* a (U+0061): L<<497.0,345.0>--<496.0,106.0>>

	* aacute (U+00E1): L<<497.0,345.0>--<496.0,106.0>>

	* abreve (U+0103): L<<497.0,345.0>--<496.0,106.0>>

	* acircumflex (U+00E2): L<<497.0,345.0>--<496.0,106.0>>

	* adieresis (U+00E4): L<<497.0,345.0>--<496.0,106.0>>

	* agrave (U+00E0): L<<497.0,345.0>--<496.0,106.0>>

	* amacron (U+0101): L<<497.0,345.0>--<496.0,106.0>>

	* aogonek (U+0105): L<<497.0,345.0>--<496.0,106.0>>

	* aring (U+00E5): L<<497.0,345.0>--<496.0,106.0>>

	* aringacute (U+01FB): L<<497.0,345.0>--<496.0,106.0>>

	* atilde (U+00E3): L<<497.0,345.0>--<496.0,106.0>>

	* dotlessi (U+0131): L<<197.0,499.0>--<198.0,0.0>>

	* fi (U+FB01): L<<578.0,499.0>--<579.0,0.0>>

	* h (U+0068): L<<198.0,382.0>--<196.0,0.0>>

	* hbar (U+0127): L<<198.0,382.0>--<196.0,0.0>>

	* hcircumflex (U+0125): L<<198.0,382.0>--<196.0,0.0>>

	* i (U+0069): L<<200.0,499.0>--<201.0,0.0>>

	* ibreve (U+012D): L<<197.0,499.0>--<198.0,0.0>>

	* ij (U+0133): L<<200.0,499.0>--<201.0,0.0>>

	* ij (U+0133): L<<494.0,504.0>--<495.0,-11.0>>

	* iogonek (U+012F): L<<200.0,499.0>--<201.0,1.0>>

	* itilde (U+0129): L<<197.0,499.0>--<198.0,0.0>>

	* j (U+006A): L<<221.0,504.0>--<222.0,-11.0>>

	* k (U+006B): L<<198.0,695.0>--<197.0,316.0>>

	* uni01C8 (U+01C8): L<<767.0,504.0>--<768.0,-11.0>>

	* uni01C9 (U+01C9): L<<487.0,504.0>--<488.0,-11.0>>

	* uni01CB (U+01CB): L<<945.0,504.0>--<946.0,-11.0>>

	* uni01CC (U+01CC): L<<819.0,504.0>--<820.0,-11.0>>

	* uni01CE (U+01CE): L<<497.0,345.0>--<496.0,106.0>>

	* uni01D0 (U+01D0): L<<197.0,499.0>--<198.0,0.0>>

	* uni0201 (U+0201): L<<497.0,345.0>--<496.0,106.0>>

	* uni0203 (U+0203): L<<497.0,345.0>--<496.0,106.0>>

	* uni0209 (U+0209): L<<197.0,499.0>--<198.0,0.0>>

	* uni020B (U+020B): L<<197.0,499.0>--<198.0,0.0>>

	* uni1E2B (U+1E2B): L<<198.0,382.0>--<196.0,0.0>>

	* uni1E2F (U+1E2F): L<<197.0,499.0>--<198.0,0.0>>

	* uni1E9E (U+1E9E): L<<211.0,435.0>--<210.0,0.0>>

	* uni1EA1 (U+1EA1): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA3 (U+1EA3): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA5 (U+1EA5): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA7 (U+1EA7): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA9 (U+1EA9): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EAB (U+1EAB): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EAD (U+1EAD): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EAF (U+1EAF): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EB1 (U+1EB1): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EB3 (U+1EB3): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EB5 (U+1EB5): L<<497.0,345.0>--<496.0,106.0>> 

	* uni1EB7 (U+1EB7): L<<497.0,345.0>--<496.0,106.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[20] PitagonSans-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 578 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 667:
less

Width = 638:
equal

Width = 658:
greater

Width = 633:
logicalnot

Width = 585:
plusminus

Width = 526:
multiply

Width = 628:
divide

Width = 580:
minus

Width = 632:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,503.0>--<142.0,506.0>> -> L<<142.0,506.0>--<447.0,728.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> 

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* section (U+00A7): B<<137.0,432.5>-<168.0,442.0>-<192.0,444.0>>/B<<192.0,444.0>-<181.0,445.0>-<165.0,457.0>> = 9.958070598460957 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* a (U+0061): L<<512.0,343.0>--<511.0,105.0>>

	* aacute (U+00E1): L<<512.0,343.0>--<511.0,105.0>>

	* abreve (U+0103): L<<512.0,343.0>--<511.0,105.0>>

	* acircumflex (U+00E2): L<<512.0,343.0>--<511.0,105.0>>

	* adieresis (U+00E4): L<<512.0,343.0>--<511.0,105.0>>

	* agrave (U+00E0): L<<512.0,343.0>--<511.0,105.0>>

	* amacron (U+0101): L<<512.0,343.0>--<511.0,105.0>>

	* aogonek (U+0105): L<<512.0,343.0>--<511.0,105.0>>

	* aring (U+00E5): L<<512.0,343.0>--<511.0,105.0>>

	* aringacute (U+01FB): L<<512.0,343.0>--<511.0,105.0>>

	* atilde (U+00E3): L<<512.0,343.0>--<511.0,105.0>>

	* dotlessi (U+0131): L<<229.0,499.0>--<230.0,0.0>>

	* fi (U+FB01): L<<626.0,499.0>--<628.0,0.0>>

	* h (U+0068): L<<229.0,367.0>--<227.0,0.0>>

	* hbar (U+0127): L<<229.0,367.0>--<227.0,0.0>>

	* hcircumflex (U+0125): L<<229.0,367.0>--<227.0,0.0>>

	* i (U+0069): L<<231.0,499.0>--<233.0,0.0>>

	* ibreve (U+012D): L<<229.0,499.0>--<230.0,0.0>>

	* ij (U+0133): L<<231.0,499.0>--<233.0,0.0>>

	* ij (U+0133): L<<542.0,508.0>--<544.0,2.0>>

	* iogonek (U+012F): L<<231.0,499.0>--<232.0,1.0>>

	* itilde (U+0129): L<<229.0,499.0>--<230.0,0.0>>

	* j (U+006A): L<<246.0,508.0>--<248.0,2.0>>

	* k (U+006B): L<<228.0,203.0>--<227.0,0.0>>

	* k (U+006B): L<<229.0,698.0>--<228.0,322.0>>

	* s (U+0073): L<<429.0,473.0>--<430.0,348.0>>

	* sacute (U+015B): L<<429.0,473.0>--<430.0,348.0>>

	* scaron (U+0161): L<<429.0,473.0>--<430.0,348.0>>

	* scedilla (U+015F): L<<429.0,473.0>--<430.0,348.0>>

	* scircumflex (U+015D): L<<429.0,473.0>--<430.0,348.0>>

	* uni01C8 (U+01C8): L<<807.0,508.0>--<809.0,2.0>>

	* uni01C9 (U+01C9): L<<536.0,508.0>--<538.0,2.0>>

	* uni01CB (U+01CB): L<<971.0,508.0>--<973.0,2.0>>

	* uni01CC (U+01CC): L<<863.0,508.0>--<865.0,2.0>>

	* uni01CE (U+01CE): L<<512.0,343.0>--<511.0,105.0>>

	* uni01D0 (U+01D0): L<<229.0,499.0>--<230.0,0.0>>

	* uni0201 (U+0201): L<<512.0,343.0>--<511.0,105.0>>

	* uni0203 (U+0203): L<<512.0,343.0>--<511.0,105.0>>

	* uni0209 (U+0209): L<<229.0,499.0>--<230.0,0.0>>

	* uni020B (U+020B): L<<229.0,499.0>--<230.0,0.0>>

	* uni0219 (U+0219): L<<429.0,473.0>--<430.0,348.0>>

	* uni1E2B (U+1E2B): L<<229.0,367.0>--<227.0,0.0>>

	* uni1E2F (U+1E2F): L<<229.0,499.0>--<230.0,0.0>>

	* uni1E61 (U+1E61): L<<429.0,473.0>--<430.0,348.0>>

	* uni1E63 (U+1E63): L<<429.0,473.0>--<430.0,348.0>>

	* uni1E65 (U+1E65): L<<429.0,473.0>--<430.0,348.0>>

	* uni1E67 (U+1E67): L<<429.0,473.0>--<430.0,348.0>>

	* uni1E69 (U+1E69): L<<429.0,473.0>--<430.0,348.0>>

	* uni1E9E (U+1E9E): L<<248.0,417.0>--<247.0,0.0>>

	* uni1EA1 (U+1EA1): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA3 (U+1EA3): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA5 (U+1EA5): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA7 (U+1EA7): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA9 (U+1EA9): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EAB (U+1EAB): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EAD (U+1EAD): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EAF (U+1EAF): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EB1 (U+1EB1): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EB3 (U+1EB3): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EB5 (U+1EB5): L<<512.0,343.0>--<511.0,105.0>> 

	* uni1EB7 (U+1EB7): L<<512.0,343.0>--<511.0,105.0>> [code: found-semi-vertical]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 36 | 76 | 698 | 37 | 525 | 0 |
| 0% | 3% | 6% | 51% | 3% | 38% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
