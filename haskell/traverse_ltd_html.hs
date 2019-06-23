-- vim: ts=4 sw=4 expandtab syntax=haskell

module TraverseHTML where

import Data.Set

type HTML = [HTML_element]
data HTML_element
    = HTML_text String
    | HTML_font Font_tag HTML
    | HTML_p HTML
data Font_tag = Font_tag (Maybe Int) (Maybe String) (Maybe Font_color)
data Font_color
    = Colour_name String
    | Hex Int
    | RGB Int Int Int

------------------------------------------------------------------------------

font_sizes_in_html :: HTML -> Set Int -> Set Int
font_sizes_in_html elements sizes =
    foldr font_sizes_in_element sizes elements

font_sizes_in_element :: HTML_element -> Set Int -> Set Int
font_sizes_in_element (HTML_text _) sizes = sizes
font_sizes_in_element (HTML_font font_tag html) sizes =
    let
        Font_tag maybe_size _ _ = font_tag
        newsizes = case maybe_size of
            Nothing ->
                sizes
            Just fontsize ->
                Data.Set.insert fontsize sizes
    in
        font_sizes_in_html html newsizes
font_sizes_in_element (HTML_p html) sizes = font_sizes_in_html html sizes

------------------------------------------------------------------------------

font_names_in_html :: HTML -> Set String -> Set String
font_names_in_html elements names =
    foldr font_names_in_element names elements

font_names_in_element :: HTML_element -> Set String -> Set String
font_names_in_element (HTML_text _) names = names
font_names_in_element (HTML_font font_tag html) names =
    let
        Font_tag _ maybe_name _ = font_tag
        newnames = case maybe_name of
            Nothing ->
                names
            Just fontname ->
                Data.Set.insert fontname names
    in
        font_names_in_html html newnames
font_names_in_element (HTML_p html) names = font_names_in_html html names

------------------------------------------------------------------------------

font_stuff_in_html :: (Font_tag -> a -> a) -> HTML -> a -> a
font_stuff_in_html f elements stuff =
    foldr (font_stuff_in_element f) stuff elements

font_stuff_in_element :: (Font_tag -> a -> a) -> HTML_element -> a -> a
font_stuff_in_element f (HTML_text _) stuff = stuff
font_stuff_in_element f (HTML_font font_tag html) stuff =
    let newstuff = f font_tag stuff in
    font_stuff_in_html f html newstuff
font_stuff_in_element f (HTML_p html) stuff =
    font_stuff_in_html f html stuff

font_sizes_in_html' :: HTML -> Set Int -> Set Int
font_sizes_in_html' html sizes =
    font_stuff_in_html accumulate_font_sizes html sizes

accumulate_font_sizes font_tag sizes =
    let Font_tag maybe_size _ _ = font_tag in
    case maybe_size of
        Nothing ->
            sizes
        Just fontsize ->
            Data.Set.insert fontsize sizes

font_names_in_html' :: HTML -> Set String -> Set String
font_names_in_html' html names =
    font_stuff_in_html accumulate_font_names html names

accumulate_font_names font_tag names =
    let Font_tag _ maybe_name _ = font_tag in
    case maybe_name of
        Nothing ->
            names
        Just fontname ->
            Data.Set.insert fontname names

------------------------------------------------------------------------------
