using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bounds : MonoBehaviour
{
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "Player projectile" || other.tag == "projectile")
        {
            Destroy(other.gameObject);
        }
    }

}
