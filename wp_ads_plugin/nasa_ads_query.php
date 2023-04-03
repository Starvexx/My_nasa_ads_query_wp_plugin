<?php # -*- coding: utf-8 -*-
/*
 * Plugin Name:  My NASA/ADS query plugin
 * Plugin URI:   https://www.nemesis.univie.ac.at
 * Description:  Since none of the plugins work, this is my own version that should at some point work.
 * Version:      0.1 beta
 * Author:       David Hernandez 
 * Author URI:   https://homepage.univie.ac.at/david.hernandez/
 * License:      GPL2
 * License URI:  https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:  my-nasaads-query-plugin
 */

add_shortcode( 'python', 'embed_python' );

function embed_python( $attributes )
{
    $data = shortcode_atts(
        [
            'file' => 'query.py'
        ],
        $attributes
    );

    $handle = popen( __DIR__ . '/' . $data['file'], 'r' );
    $read = '';

    while ( ! feof( $handle ) )
    {
        $read .= fread( $handle, 2096 );
    }

    pclose( $handle );

    return $read;
}
